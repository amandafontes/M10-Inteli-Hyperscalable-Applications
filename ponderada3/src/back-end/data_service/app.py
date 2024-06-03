from flask import Flask
from flask_migrate import Migrate
from config import Config
from models import db
from routes import data_blueprint

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(data_blueprint, url_prefix='/data')

if __name__ == '__main__':
    app.run(debug=True)
