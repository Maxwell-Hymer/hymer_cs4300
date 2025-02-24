from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth import logout
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# Create your views here.
# ViewSet for handling Movie API requests
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# ViewSet for handling Seat API requests
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

# ViewSet for handling Booking API requests
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Renders the list of movies
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

# Handle seat booking for specific movies
def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    available_seats = Seat.objects.filter(booking_status=False)

    if request.method == 'POST':
        selected_seats = request.POST.getlist('seats') 
        for seat_id in selected_seats:
            seat = Seat.objects.get(id=seat_id)
            if not seat.booking_status: 
                seat.booking_status = True
                seat.save()
                Booking.objects.create(movie=movie, seat=seat, user=request.user)
        
        return redirect('/booking-history/')

    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'available_seats': available_seats,
    })

# Render the booking history for the user
def booking_history(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})

# Handle user signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Custom logout view
def custom_logout_view(request):
    logout(request)
    return redirect('/')