from django.shortcuts import redirect, render

import auction
from .models import Auction, Bid
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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


def place_bid(request, item_id):
    item = Auction.objects.get(pk=item_id)
    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        bid_amount = request.POST['bid_amount']
        bid = Bid(amount=bid_amount, auction=item, user=user)
        bid.save()
        message = 'Bid placed successfully'
        return render(request, 'auction/placebid.html', {'item': item, 'message': message})
    return render(request, 'auction/placebid.html', {'item': item})

def user_register(request):
    message = ""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            message = "Invalid credentials"
    else:
        form = UserCreationForm()
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'auction/register.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'auction/login.html')

def logout_view(request):
    logout(request) 
    return redirect('home')       