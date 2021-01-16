# -*- coding: utf-8 -*-
"""The main entry into the website"""
from flask import Flask
from app.config import Config
from app.model import DB

# initialize the app
APP = Flask(__name__)
APP.config.from_object(Config)


# init DB and login manager
DB.init_app(APP)

# needs to be imported at end to avoid circular dependency
from app.views import *
from app.error_handling import handle_generic_error
