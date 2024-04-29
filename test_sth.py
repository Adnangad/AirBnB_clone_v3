#!/usr/bin/python3
from models.state import State
from models.review import Review
from models import storage
import sys

# Retrieve all city objects
city_objects = list(storage.all(Review).values())

# Print each city object
for city in city_objects:
    print(city)

