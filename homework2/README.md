Project Title:
Movie Theater Booking Web Application

Description:
This is a Django-based RESTful movie theater booking application that allows users to view movie listings, book seats, and check their booking history. 
The application uses Django REST Framework (DRF) for the API and Bootstrap for the user interface.

Features:
View Movie Listings: User can see a list of available movies that they can book seats for
Book Seats: Users can book seats for a specific movie
Bookin History: Users can see their booking history
User Authentication: Users can log in/out and sign up

Prerequisites:
- Python 3.8 or higher
- pip (python package manager)
- Git (optional, for version control)

Setup Instructions:
1. Clone the Repo:
    git clone https://github.com/Maxwell-Hymer/hymer_cs4300/homework2.git
    cd homework2/movie_theater_booking

2. Set Up a Virtual Environment:
    python3 -m venv myenv
    source myenv/bin.activate

3. Install Dependencies:
    pip install django djangorestframework

4. Set Up Database:
    python manage.py migrate

5. Create a Super User:
    python manage.py createsuperuser

6. Run Tests
    python manage.py test

7. Run Development Server:
    python manage . py runserver 0.0.0.0:3000

API Endpoints:
The application uses the following API endpoints:
- Movies: /api/movies/
- Seats: /api/seats/
- Bookings: /api/bookings/

Acknowledgements:
- Django Documentation: https://docs.djangoproject.com/en/stable/
- Django REST Framework Documentation: https://www.django-rest-framework.org/
- Boostrap Documentation: https://getbootstrap.com/docs/5.3/getting-started/introduction/
- Testing Documentation: https://docs.djangoproject.com/en/stable/topics/testing/

Contact:
Maxwell Hymer
mhymer@uccs.edu
Maxwell-Hymer
