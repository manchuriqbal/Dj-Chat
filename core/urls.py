from django.contrib.auth import views as auth_view
from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('signup/', views.signup, name="signup"),
    path('logout/', auth_view.LogoutView.as_view(), name="logout"),
    path('login/', auth_view.LoginView.as_view(template_name='core/login.html'), name="login"),
]
