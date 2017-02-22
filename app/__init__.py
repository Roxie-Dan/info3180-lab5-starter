from flask import Flask
from flask_wtf import Form
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "make money not enemies"
app.config['SQLALCHEMY_lab5_URI'] = "postgresql://lab5:love@localhost/database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)

app.config.from_object(__name__)
from app import views
