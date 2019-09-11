from django.urls import path
from . import views
app_name = 'db_ops'

urlpatterns = [
    path('', views.get_locations)
]
