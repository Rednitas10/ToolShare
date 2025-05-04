# backend/listings/serializers.py
from rest_framework import serializers
from .models import Listing, ListingImage, Booking

class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = ["id", "image"]

class ListingSerializer(serializers.ModelSerializer):
    images = ListingImageSerializer(many=True, read_only=True)
    owner  = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Listing
        fields = [
            "id", "owner", "title", "description",
            "category", "price_per_day", "location",
            "images", "created_at",
        ]

class BookingSerializer(serializers.ModelSerializer):
    renter  = serializers.ReadOnlyField(source="renter.username")
    listing = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all())

    class Meta:
        model = Booking
        fields = [
            "id", "listing", "renter", "start_date",
            "end_date", "total_price", "status",
            "stripe_session_id", "created_at",
        ]
        read_only_fields = ["status", "stripe_session_id", "created_at"]
