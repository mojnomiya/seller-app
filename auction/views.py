from django.shortcuts import render
from .models import Auction, Bid
from django.utils import timezone

def home(request):
    active_auctions = Auction.objects.filter(end_time__gt=timezone.now())
    return render(request, 'auction/index.html', {'active_auctions': active_auctions})

def admin_auction_status(request):
    auctions = Auction.objects.all()
    auction_data = []
    
    for auction in auctions:
        highest_bid = Bid.objects.filter(auction=auction).order_by('-amount').first()
        auction_data.append({
            'auction': auction,
            'highest_bid': highest_bid,
        })
    
    return render(request, 'auction/admin_auctions.html', {'auction_data': auction_data})
