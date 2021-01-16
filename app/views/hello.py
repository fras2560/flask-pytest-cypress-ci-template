# -*- coding: utf-8 -*-
"""Holds a simple hello world view."""
from flask import render_template
from app import APP
from app.model import Entity
from app.errors import NotFoundException


@APP.route("/")
def hello_world():
    return render_template("hello_world.html")


@APP.route("/<int:entity_id>")
def hello_world_entity(entity_id):
    entity = Entity.query.get(entity_id)
    if entity is None:
        raise NotFoundException(f"Sorry, entity not found - {entity_id}")
    return render_template("hello_world.html", entity=entity)
