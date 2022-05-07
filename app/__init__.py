from flask import Flask
from config import config_options


# App initialization
app = Flask(__name__)
from app import views

# Setting up Configuration
app.config.from_object(config_options)

