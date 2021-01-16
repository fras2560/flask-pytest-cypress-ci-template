# -*- coding: utf-8 -*-
"""Holds configuration for the app."""
import os
from uuid import uuid1


class Config(object):
    URL = os.environ.get("DATABASE_URL", "sqlite://")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite://")
    SECRET_KEY = os.environ.get("SECRET_KEY", str(uuid1()))
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USE_SESSION_FOR_NEXT = True
    TESTING = os.environ.get("TESTING", False)
    DEBUG = os.environ.get("DEBUG", False)


class TestConfig(object):
    URL = "sqlite://"
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SECRET_KEY = str(uuid1())
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USE_SESSION_FOR_NEXT = True
    TESTING = True
    DEBUG = True
