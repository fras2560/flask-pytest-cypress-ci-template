# -*- coding: utf-8 -*-
"""The main entry into the website"""
import pytest
from app import APP
from initDB import init_database
from app.config import TestConfig


@pytest.fixture
def client():
    APP.config.from_object(TestConfig)
    with APP.test_client() as client:
        init_database()
        yield client
