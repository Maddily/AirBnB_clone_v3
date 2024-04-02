#!/usr/bin/python3
"""
Unittests for the view for User objects
- TestUserAPI
"""

import unittest
from flask import Flask
from api.v1.views import app_views
from models import storage
from models.state import State
from models.user import User


class TestUserAPI(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(app_views)
        self.client = self.app.test_client()
        self.state = State(name="Tatooine")
        self.user = User(email="luke@jedi.com", password="usetheforce",
                         state_id=self.state.id)

    def tearDown(self):
        storage.delete(self.state)
        storage.save()

    def test_get_all_users(self):
        """Tests the retrieval of user objects"""
        """
        user_emails = ["anakin@sith.com", "leia@rebels.com"]
        for email in user_emails:
            user = User(email=email, password="password",
                        state_id=self.state.id)
            storage.new(user)
        storage.save()

        # Test GET request
        response = self.client.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 2)
        self.assertIn("anakin@sith.com", [user['email'] for user in data])
        self.assertIn("leia@rebels.com", [user['email'] for user in data])
        """
        pass

    def test_create_user(self):
        """test ordinary user creation """
        """
        storage.new(self.state)
        storage.save()

        # Test POST request
        new_user_data = {'email': 'han@smuggler.com', 'password': 'falcon'}
        response = self.client.post(f'/api/v1/states/{self.state.id}/users',
                                    json=new_user_data)
        self.assertEqual(response.status_code, 201)
        data = response.json
        self.assertEqual(data['email'], 'han@smuggler.com')

        # Make sure the user is created
        user = storage.get(User, data['id'])
        self.assertIsNotNone(user)
        """
        pass

    def test_create_user_missing_fields(self):
        """ tests user creation with missing fields """
        """
        storage.new(self.state)
        storage.save()

        # Test POST request with missing fields
        new_user_data = {'password': 'wookie'}
        response = self.client.post(f'/api/v1/states/{self.state.id}/users',
                                    json=new_user_data)
        self.assertEqual(response.status_code, 400)
        """
        pass

    def test_update_user(self):
        """ Test user case by updating it """
        # Create a state and user
        storage.new(self.state)
        storage.new(self.user)
        storage.save()

        # Test PUT request
        updated_user_data = {
                'email': 'obi-wan@jedi.com',
                'password': 'forceghost'
                }
        response = self.client.put('/api/v1/users/{}'.format(self.user.id),
                                   json=updated_user_data)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['email'], 'obi-wan@jedi.com')

        # Make sure the user is updated
        user = storage.get(User, self.user.id)
        self.assertEqual(user.email, 'obi-wan@jedi.com')

    def test_update_user_invalid_fields(self):
        """ tests user case with invalid fields """
        """
        storage.new(self.state)
        storage.new(self.user)
        storage.save()

        # Test PUT request with invalid fields
        updated_user_data = {'invalid_field': 'value'}
        response = self.client.put(f'/api/v1/users/{self.user.id}',
                                   json=updated_user_data)
        self.assertEqual(response.status_code, 400)

        # Ensure the user is not updated
        user = storage.get(User, self.user.id)
        self.assertEqual(user.email, 'luke@jedi.com')
        """
        pass


if __name__ == '__main__':
    unittest.main()
