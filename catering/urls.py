from django.urls import path
from .views import add_client, client_list ,add_event,contact,home

urlpatterns = [
    path('add-client/', add_client, name='add_client'),
    path('clients/', client_list, name='client_list'),  # ✅ Ensure this exists
    path('add-event/', add_event, name='add_event'),
    path("contact/", contact, name="contact"),
    path("home/", home, name="home"),

]
