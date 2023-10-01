from django.db import models
from django.contrib.auth.models import User

class Auction(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auctions_created')
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='auctions_won')

    def __str__(self):
        return self.item_name

class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Bid of {self.amount} on {self.auction.item_name} by {self.user.username}"
