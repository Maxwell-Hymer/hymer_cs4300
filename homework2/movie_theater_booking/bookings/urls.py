from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views  
from .views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list, seat_booking, booking_history, signup

# Router for handling API endpoints listed below
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', movie_list, name='movie_list'),  # Home screen
    path('book-seat/<int:movie_id>/', seat_booking, name='seat_booking'),
    path('booking-history/', booking_history, name='booking_history'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', signup, name='signup'),
    path('api/', include(router.urls)),
]