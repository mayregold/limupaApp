from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import send_email

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('seller-dashboard/', views.seller_dashboard, name='seller_dashboard'), 
    path('buyer-dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
    path('send-email/', send_email, name='send_email'),
]