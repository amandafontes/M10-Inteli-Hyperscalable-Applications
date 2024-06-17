from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import select
from database import database, engine, metadata
from models import users
from schemas import UserCreate, UserOut, UserLogin
from utils import hash_password, verify_password
from auth import create_access_token, decode_access_token, Token
from datetime import timedelta

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.on_event("startup")
async def startup():
    await database.connect()
    metadata.create_all(engine)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/register", response_model=UserOut)
async def register(user: UserCreate):
    query = users.insert().values(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        roles="user"
    )
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id, "roles": "user"}

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    query = users.select().where(users.c.email == form_data.username)
    user = await database.fetch_one(query)
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    token_data = decode_access_token(token)
    if token_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    query = users.select().where(users.c.email == token_data.email)
    user = await database.fetch_one(query)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(current_user: UserOut = Depends(get_current_user)):
    if current_user["roles"] != "user":
        raise HTTPException(status_code=400, detail="Not a user")
    return current_user

async def get_current_admin_user(current_user: UserOut = Depends(get_current_user)):
    if current_user["roles"] != "admin":
        raise HTTPException(status_code=400, detail="Not an admin")
    return current_user

@app.get("/user", response_model=UserOut)
async def read_users_me(current_user: UserOut = Depends(get_current_active_user)):
    return current_user

@app.get("/admin", response_model=UserOut)
async def read_users_admin(current_user: UserOut = Depends(get_current_admin_user)):
    return current_user
