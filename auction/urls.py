from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('admin/auctions/', views.admin_auction_status, name='admin_auctions'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
