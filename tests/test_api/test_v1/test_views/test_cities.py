#!/usr/bin/python3
"""
Unittests for the view for City objects
- TestCityAPI
"""

import unittest
from flask import Flask
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City


class TestCityAPI(unittest.TestCase):
    """
    Test cases for the view for City objects.
    """

    def setUp(self):
        """
        Set up test client, Flask app, and initialize test data.
        """
        self.app = Flask(__name__)
        self.app.register_blueprint(app_views)
        self.client = self.app.test_client()
        self.state = State(name="California")
        self.city = City(name="San Francisco", state_id=self.state.id)

    def tearDown(self):
        """
        Clean up after each test.
        """
        storage.delete(self.state)
        storage.save()

    def test_get_cities_by_state(self):
        """
        Test retrieving cities by state.
        """
        # Create a state
        storage.new(self.state)
        storage.save()

        # Create cities
        city_names = ["Los Angeles", "San Diego"]
        for name in city_names:
            city = City(name=name, state_id=self.state.id)
            storage.new(city)
        storage.save()

        # Test GET request
        response = self.client.get('/api/v1/states/{}/cities'.format(
            self.state.id))
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 2)
        self.assertIn("Los Angeles", [city['name'] for city in data])
        self.assertIn("San Diego", [city['name'] for city in data])

    def test_get_city(self):
        """
        Test retrieving a city by its ID.
        """
        # Create a state and city
        storage.new(self.state)
        storage.new(self.city)
        storage.save()

        # Test GET request
        response = self.client.get('/api/v1/cities/{}'.format(self.city.id))
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['name'], "San Francisco")

    def test_delete_city(self):
        """
        Test deleting a city by its ID.
        """
        # Create a state and city
        storage.new(self.state)
        storage.new(self.city)
        storage.save()

        # Test DELETE request
        response = self.client.delete('/api/v1/cities/{}'.format(self.city.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {})

        # Make sure the city is deleted
        city = storage.get(City, self.city.id)
        self.assertIsNone(city)

    def test_create_city(self):
        """
        Test creating a new city.
        """
        # Create a state
        storage.new(self.state)
        storage.save()

        # Test POST request
        new_city_data = {'name': 'San Jose'}
        response = self.client.post('/api/v1/states/{}/cities'.format(
            self.state.id),
                                    json=new_city_data)
        self.assertEqual(response.status_code, 201)
        data = response.json
        self.assertEqual(data['name'], 'San Jose')

        # Make sure the city is created
        city = storage.get(City, data['id'])
        self.assertIsNotNone(city)

    def test_update_city(self):
        """
        Test updating an existing city.
        """
        # Create a state and city
        storage.new(self.state)
        storage.new(self.city)
        storage.save()

        # Test PUT request
        updated_city_data = {'name': 'Los Angeles'}
        response = self.client.put('/api/v1/cities/{}'.format(self.city.id),
                                   json=updated_city_data)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['name'], 'Los Angeles')

        # Make sure the city is updated
        city = storage.get(City, self.city.id)
        self.assertEqual(city.name, 'Los Angeles')


if __name__ == '__main__':
    unittest.main()
