#!/usr/bin/python3
""" holds class Amenity"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Representation of Amenity """

    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""

        super().__init__(*args, **kwargs)
