# backend/listings/admin.py
from django.contrib import admin
from .models import Listing, ListingImage, Booking

admin.site.register(Listing)
admin.site.register(ListingImage)
admin.site.register(Booking)
