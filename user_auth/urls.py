from django.urls import path 
from . import views
urlpatterns = [
    path('login_/', views.login_, name='login_'),
    path('register/', views.register, name='register'),
    path('logout_/', views.logout_, name='logout_'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/<int:pk>', views.update_profile, name='update_profile'),
    path('reset_password/', views.reset_password,name='reset_password'),
]
