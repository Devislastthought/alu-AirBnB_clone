#!/usr/bin/python3
"""The User model."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represent a person using the application."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
