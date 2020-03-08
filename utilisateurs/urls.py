from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from utilisateurs.views import user_logout

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", user_logout, name="logout")
]
