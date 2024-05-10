from django.urls import path
from . import views
import debug_toolbar

# URLconf
urlpatterns = [
    path('hello/', views.say_hello),
]
