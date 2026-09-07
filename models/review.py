#!/usr/bin/python3
"""The Review model."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review written about a place."""

    place_id = ""
    user_id = ""
    text = ""
