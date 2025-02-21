from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet

# Initialize a router and assign our viewsets with it
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

# API URLs determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
