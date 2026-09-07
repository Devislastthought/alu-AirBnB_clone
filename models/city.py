#!/usr/bin/python3
"""The City model."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city in a state."""

    state_id = ""
    name = ""
