from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("email", String(50), unique=True, index=True),
    Column("password", String(128)),
    Column("roles", String(50)),
    Column("criado_em", DateTime, default=func.now()),
    Column("atualizado_em", DateTime, default=func.now(), onupdate=func.now())
)
