# -*- coding: utf-8 -*-
"""Holds a database model for the application."""
from flask_sqlalchemy import SQLAlchemy

"""The database object."""
DB = SQLAlchemy()


class Entity(DB.Model):
    """
        A class used to store some entity information
        Columns:
            id: the unique id
            name: the name of the entity
    """
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(256))

    def __init__(self, name: str):
        self.name = name

    def json(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
        }

    def __str__(self):
        return self.name
