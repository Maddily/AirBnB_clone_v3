#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

new_state = State()
new_state.name = "California"
storage.new(new_state)
storage.save()

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))