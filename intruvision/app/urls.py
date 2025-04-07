from django.urls import path
from . import views  # Ensure this is correct
from .import views
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('admin_home', views.admin_home),
    path('change_passkey', views.change_passkey),
    path('view_appreview_and_rating', views.view_appreview_and_rating),
    path('view_users', views.view_users),
    path('view_complaints_sendreply', views.view_complaints_sendreply),
]
