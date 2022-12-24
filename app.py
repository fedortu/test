from flask import Flask
from flask_migrate import Migrate
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
# manager = Manager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)