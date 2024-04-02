#!/usr/bin/python3
"""Unit tests for states module"""

import inspect
import pep8
import unittest
import os
from api.v1.views import app_views
from models import storage
from flask import Flask
from models.state import State
from api.v1.views import states


class TestStates(unittest.TestCase):
    """Tests states module"""

    def setUp(self):
        """Creates an app and State object"""

        self.app = Flask(__name__)
        self.app.register_blueprint(app_views)
        self.client = self.app.test_client()
        self.state = State(name="California")

    def tearDown(self):
        """Deletes created state"""

        storage.delete(self.state)
        storage.save()

    def test_doc(self):
        """Tests module docstring existence"""

        self.assertIsNotNone(states.__doc__)

    def test_function_doc(self):
        """Tests function docstring existence (for all functions)"""

        functions = inspect.getmembers(states, inspect.isfunction)
        for function in functions:
            self.assertIsNotNone(function[1].__doc__)

    def test_pep8(self):
        """Tests if module follows PEP8 style"""

        pep8style = pep8.StyleGuide(quiet=True)
        errors = pep8style.check_files(['api/v1/views/states.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_executable(self):
        """Tests if the file is executable"""

        file_stat = os.stat('api/v1/views/states.py')
        permissions = str(oct(file_stat[0]))
        expected = int(permissions[5:-2]) >= 5
        self.assertTrue(expected)

    def test_get_state(self):
        """Tests GET request"""

        storage.new(self.state)
        storage.save()

        response = self.client.get('/api/v1/states/{}'.format(self.state.id))
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['name'], "California")

    def test_delete_state(self):
        """Tests DELETE request"""

        storage.new(self.state)
        storage.save()

        response = self.client.delete('/api/v1/states/{}'.format(self.state.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {})

        state = storage.get(State, self.state.id)
        self.assertIsNone(state)

    def test_create_state(self):
        """Tests POST request"""

        storage.new(self.state)
        storage.save()

        data = {'name': 'Twilight'}
        response = self.client.post('/api/v1/states/', json=data)
        self.assertEqual(response.status_code, 201)
        data = response.json
        self.assertEqual(data['name'], 'Twilight')

        state = storage.get(State, data['id'])
        self.assertIsNotNone(state)

    def test_update_state(self):
        """Tests PUT request"""

        storage.new(self.state)
        storage.save()

        data = {'name': 'Twilight'}
        response = self.client.put('/api/v1/states/{}'.format(self.state.id),
                                   json=data)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['name'], 'Twilight')

        state = storage.get(State, self.state.id)
        self.assertEqual(state.name, 'Twilight')


if __name__ == "__main__":
    unittest.main()
