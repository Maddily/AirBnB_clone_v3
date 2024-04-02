#!/usr/bin/python3
"""Unit tests for amenities module"""

import inspect
import pep8
import unittest
import os
from api.v1.views import app_views
from models import storage
from flask import Flask
from models.amenity import Amenity
from api.v1.views import amenities


class TestAmenities(unittest.TestCase):
    """Tests amenities module"""

    def setUp(self):
        """Creates an app and Amenity object"""

        self.app = Flask(__name__)
        self.app.register_blueprint(app_views)
        self.client = self.app.test_client()
        self.amenity = Amenity(name="TV")

    def tearDown(self):
        """Deletes created amenity"""

        storage.delete(self.amenity)
        storage.save()

    def test_doc(self):
        """Tests module docstring existence"""

        self.assertIsNotNone(amenities.__doc__)

    def test_function_doc(self):
        """Tests function docstring existence (for all functions)"""

        functions = inspect.getmembers(amenities, inspect.isfunction)
        for function in functions:
            self.assertIsNotNone(function[1].__doc__)

    def test_pep8(self):
        """Tests if module follows PEP8 style"""

        pep8style = pep8.StyleGuide(quiet=True)
        errors = pep8style.check_files(['api/v1/views/amenities.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_executable(self):
        """Tests if the file is executable"""

        file_stat = os.stat('api/v1/views/amenities.py')
        permissions = str(oct(file_stat[0]))
        expected = int(permissions[5:-2]) >= 5
        self.assertTrue(expected)

    def test_get_amenity(self):
        """Tests GET request"""

        storage.new(self.amenity)
        storage.save()

        response = self.client.get('/api/v1/amenities/{}'.format(
            self.amenity.id))
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['name'], "TV")

    def test_delete_amenity(self):
        """Tests DELETE request"""

        storage.new(self.amenity)
        storage.save()

        response = self.client.delete('/api/v1/amenities/{}'.format(
            self.amenity.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {})

        amenity = storage.get(Amenity, self.amenity.id)
        self.assertIsNone(amenity)

    def test_create_amenity(self):
        """Tests POST request"""

        storage.new(self.amenity)
        storage.save()

        data = {'name': 'Wifi'}
        response = self.client.post('/api/v1/amenities/', json=data)
        self.assertEqual(response.status_code, 201)
        data = response.json
        self.assertEqual(data['name'], 'Wifi')

        amenity = storage.get(Amenity, data['id'])
        self.assertIsNotNone(amenity)

    def test_update_amenity(self):
        """Tests PUT request"""

        storage.new(self.amenity)
        storage.save()

        data = {'name': 'Wifi'}
        response = self.client.put('/api/v1/amenities/{}'.format(
            self.amenity.id),
                                   json=data)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['name'], 'Wifi')

        amenity = storage.get(Amenity, self.amenity.id)
        self.assertEqual(amenity.name, 'Wifi')


if __name__ == "__main__":
    unittest.main()
