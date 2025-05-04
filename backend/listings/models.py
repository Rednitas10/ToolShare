# backend/listings/models.py
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Listing(models.Model):
    owner         = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title         = models.CharField(max_length=200)
    description   = models.TextField()
    category      = models.CharField(max_length=50)
    price_per_day = models.DecimalField(max_digits=7, decimal_places=2)
    location      = models.CharField(max_length=200)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.owner}"

class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="images")
    image   = models.ImageField(upload_to="listings/")

class Booking(models.Model):
    STATUS_CHOICES = [
        ("pending",   "Pending"),
        ("approved",  "Approved"),
        ("declined",  "Declined"),
        ("completed", "Completed"),
    ]

    listing           = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bookings")
    renter            = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    start_date        = models.DateField()
    end_date          = models.DateField()
    total_price       = models.DecimalField(max_digits=8, decimal_places=2)
    status            = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    stripe_session_id = models.CharField(max_length=255, blank=True, null=True)
    created_at        = models.DateTimeField(auto_now_add=True)
