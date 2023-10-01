from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('admin/auctions/', views.admin_auction_status, name='admin_auctions'),
]
