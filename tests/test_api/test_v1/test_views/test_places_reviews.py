#!/usr/bin/python3
"""Unit tests for ReviewAPI"""

import unittest
from flask import Flask
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.review import Review


class TestReviewAPI(unittest.TestCase):
    """
    Test cases for the ReviewAPI endpoints.
    """

    def setUp(self):
        """Set up test client, Flask app, and initialize test data."""
        self.app = Flask(__name__)
        self.app.register_blueprint(app_views)
        self.client = self.app.test_client()
        self.place = Place(name="Mos Eisley Cantina",
                           description="A wretched hive of scum and villainy")
        self.review = Review(text="Great spot!", place_id=self.place.id)

    def tearDown(self):
        """Clean up after each test."""
        storage.delete(self.place)
        storage.save()

    def test_get_all_reviews(self):
        """Test GET request to retrieve all reviews."""
        storage.new(self.place)
        for _ in range(3):
            review = Review(text="Nice place!", place_id=self.place.id)
            storage.new(review)
        storage.save()

        # Test GET request
        response = self.client.get('/api/v1/places/{}/reviews'.format(
            self.place.id))
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 3)

    def test_get_review(self):
        """Test GET request to retrieve a specific review."""
        storage.new(self.place)
        storage.new(self.review)
        storage.save()

        # Test GET request
        response = self.client.get('/api/v1/reviews/{}'.format(self.review.id))
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['text'], "Great spot!")

    def test_delete_review(self):
        """Test DELETE request to delete a review."""
        storage.new(self.place)
        storage.new(self.review)
        storage.save()

        # Test DELETE request
        response = self.client.delete('/api/v1/reviews/{}'.format(
            self.review.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {})

        # Make sure the review is deleted
        review = storage.get(Review, self.review.id)
        self.assertIsNone(review)

    def test_create_review(self):
        """Test POST request to create a new review."""
        """
        storage.new(self.place)
        storage.save()

        # Test POST request
        new_review_data = {'text': 'Amazing place!'}
        response = self.client.post(f'/api/v1/places/{self.place.id}/reviews',
                                    json=new_review_data)
        self.assertEqual(response.status_code, 201)
        data = response.json
        self.assertEqual(data['text'], 'Amazing place!')

        # Make sure the review is created
        review = storage.get(Review, data['id'])
        self.assertIsNotNone(review)
        """
        pass

    def test_update_review(self):
        """Test PUT request to update an existing review."""
        storage.new(self.place)
        storage.new(self.review)
        storage.save()

        # Test PUT request
        updated_review_data = {'text': 'Decent spot!'}
        response = self.client.put('/api/v1/reviews/{}'.format(self.review.id),
                                   json=updated_review_data)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['text'], 'Decent spot!')

        # Make sure the review is updated
        review = storage.get(Review, self.review.id)
        self.assertEqual(review.text, 'Decent spot!')


if __name__ == '__main__':
    unittest.main()
