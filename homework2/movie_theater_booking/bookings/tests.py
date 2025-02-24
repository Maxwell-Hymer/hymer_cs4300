from django.test import TestCase
from .models import Movie, Seat, Booking
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from datetime import timedelta

# Create your tests here.
class MovieModelTest(TestCase):
    # Set up test environment for Movie model tests
    def setUp(self):
        # Initialize test Movie instance for testing
        self.movie = Movie.objects.create(
            title = "Pacific Rim",
            description = "Giant robots vs giant aliens",
            release_date = "2013-07-12",
            duration = timedelta(hours=2, minutes=12)
        )

    # Test the creation of the Movie instance
    def test_movie_creations(self):
        # Checks the movie title and description are correct
        self.assertEqual(self.movie.title, "Pacific Rim")
        self.assertEqual(self.movie.description, "Giant robots vs giant aliens")

class SeatModelTest(TestCase):
    # Set up test environment for Seat Model tests
    def setUp(self):
        self.seat = Seat.objects.create(seat_number="E8")
    
    # Test the creation of the Seat instance
    def test_seat_creation(self):
        # Checks the Seat number and booking status are correct
        self.assertEqual(self.seat.seat_number, "E8")
        self.assertFalse(self.seat.booking_status)

class BookingModelTest(TestCase):
    # Set up test environment for Booking Model tests
    def setUp(self):
        # Initialize test user object
        self.user = User.objects.create_user(username='test_user', password='test_pass')
        # Initialize sample Movie instance to test
        self.movie = Movie.objects.create(
            title = "Pacific Rim",
            description = "Giant robots vs giant aliens",
            release_date = "2013-07-12",
            duration = timedelta(hours=2, minutes=12)
        )
        # Initialize a sample Seat instance to test
        self.seat = Seat.objects.create(seat_number='E8')
        # Initialize a Booking instance to test
        self.booking = Booking.objects.create(movie=self.movie, seat=self.seat, user=self.user)

    # Test the creation of a Booking instance
    def test_booking_creation(self):
        # Checks if the Bookings movie, Seat, and user are correct
        self.assertEqual(self.booking.movie.title, "Pacific Rim")
        self.assertEqual(self.booking.seat.seat_number, "E8")
        self.assertEqual(self.booking.user.username, "test_user")

class APITests(APITestCase):
    # Initialize the test environment for API tests
    def setUp(self):
        # Create a superuser to avoid 403 Forbidden responses during API tests
        self.user = User.objects.create_superuser(username='test_user', password='test_pass')
        # Initialize a sample movie instance to test
        self.movie = Movie.objects.create(
            title = "Pacific Rim",
            description = "Giant robots vs giant aliens",
            release_date = "2013-07-12",
            duration = timedelta(hours=2, minutes=12)
        )
        # Initialize a sample seat instance to test
        self.seat = Seat.objects.create(seat_number="E8")
        # Initialize a sample movie instance to test
        self.booking = Booking.objects.create(movie=self.movie, seat=self.seat, user=self.user)

    # Test the movie list API endpoint
    def test_movie_list(self):
        response = self.client.get(reverse('movie-list'))
        # Check if the response status code is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the response data contains a movie
        self.assertEqual(len(response.data), 1)

    # Test the seat list API endpoint
    def test_seat_list(self):
        response = self.client.get(reverse('seat-list'))
        # Check if the response status code is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the response contains a seat
        self.assertEqual(len(response.data), 1)

    # Test the booking creation API endpoint
    def test_booking_creation(self):
        # Log in the test user
        self.client.login(username='test_user', password='test_pass')
        # Attempt to create a new booking via the API
        response = self.client.post(reverse('booking-list'), {
            'movie': self.movie.id,
            'seat': self.seat.id,
            'user': self.user.id
        })
        # Checks if response status code is 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Checks if the number of bookings has increased by 1
        self.assertEqual(Booking.objects.count(), 2)
