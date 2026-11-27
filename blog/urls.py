# blog\urls.py

from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path(
        'profile/password/',
        views.PasswordChangeView.as_view(),
        name='password_change'
    ),
]
