from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list, seat_booking, booking_history

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', movie_list, name='movie_list'),  # Home page (this is the movie list)
    path('book-seat/<int:movie_id>/', seat_booking, name='seat_booking'),  # Booking page
    path('booking-history/', booking_history, name='booking_history'),  # Booking history page
    path('api/', include(router.urls)),  # Include the API URLs
]