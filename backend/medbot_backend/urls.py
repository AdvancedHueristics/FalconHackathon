from django.urls import path
from . import views
from medbot_backend.controllers.loginController import signup, validate_user

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('validate_user/', validate_user, name='validate_user'),
]