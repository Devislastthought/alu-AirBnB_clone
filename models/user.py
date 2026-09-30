#!/usr/bin/python3
"""Module defining the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user of the AirBnB clone."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
