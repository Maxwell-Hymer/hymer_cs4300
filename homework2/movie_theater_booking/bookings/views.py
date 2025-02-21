from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.Objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.Objects.all()
    serializer_class = SeatSerializer

    # Option to filter seats via availability or another criteria
    def get_queryset(self):
        return super().get_queryset().filter(booking_status=False)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.Objects.all()
    serializer_class = BookingSerializer

    # Optionally filter bookings for active user
    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user)