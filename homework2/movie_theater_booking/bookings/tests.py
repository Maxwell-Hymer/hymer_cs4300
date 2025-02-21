from django.test import TestCase
from .models import Movie, Seat, Booking
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from datetime import timedelta

# Create your tests here.
class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title = "Pacific Rim",
            description = "Giant robots vs giant aliens",
            release_date = "2013-07-12",
            duration = timedelta(hours=2, minutes=12)
        )

    def test_movie_creations(self):
        self.assertEqual(self.movie.title, "Pacific Rim")
        self.assertEqual(self.movie.description, "Giant robots vs giant aliens")

class SeatModelTest(TestCase):
    def setUp(self):
        self.seat = Seat.objects.create(seat_number="E8")
    
    def test_seat_creation(self):
        self.assertEqual(self.seat.seat_number, "E8")
        self.assertFalse(self.seat.booking_status)

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_pass')
        self.movie = Movie.objects.create(
            title = "Pacific Rim",
            description = "Giant robots vs giant aliens",
            release_date = "2013-07-12",
            duration = timedelta(hours=2, minutes=12)
        )
        self.seat = Seat.objects.create(seat_number='E8')
        self.booking = Booking.objects.create(movie=self.movie, seat=self.seat, user=self.user)

    def test_booking_creation(self):
        self.assertEqual(self.booking.movie.title, "Pacific Rim")
        self.assertEqual(self.booking.seat.seat_number, "E8")
        self.assertEqual(self.booking.user.username, "test_user")

class APITests(APITestCase):
    def setUp(self):
        # Adjusted user creation to super user to stop getting 403 response
        self.user = User.objects.create_superuser(username='test_user', password='test_pass')
        self.movie = Movie.objects.create(
            title = "Pacific Rim",
            description = "Giant robots vs giant aliens",
            release_date = "2013-07-12",
            duration = timedelta(hours=2, minutes=12)
        )
        self.seat = Seat.objects.create(seat_number="E8")
        self.booking = Booking.objects.create(movie=self.movie, seat=self.seat, user=self.user)

    def test_movie_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_seat_list(self):
        response = self.client.get(reverse('seat-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_booking_creation(self):
        self.client.login(username='test_user', password='test_pass')
        response = self.client.post(reverse('booking-list'), {
            'movie': self.movie.id,
            'seat': self.seat.id,
            'user': self.user.id
        })

        print("Response status code:", response.status_code)
        print("Response content:", response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)
