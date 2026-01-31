from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.booking, name='booking'),
    path('history/', views.history, name='history'),
    path('support/', views.support, name='support'),
    path('about/', views.about, name='about'),
    path('bookNow/<int:pk>', views.bookNow, name='bookNow'),
    path('delete_/<int:pk>', views.delete_, name='delete_'),
    path('delete_permanently/<int:pk>',views.delete_permanently, name='delete_permanently'),
    path('restore/<int:pk>', views.restore, name='restore'),
    path('restore_all/', views.restore_all, name='restore_all'),
    path('delete_all/', views.delete_all, name='delete_all'),
]
