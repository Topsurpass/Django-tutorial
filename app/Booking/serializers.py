from rest_framework import serializers
from .models import Booking
from app.Property.serializers import PropertySerializer
from datetime import date
class BookingSerializer(serializers.ModelSerializer):
    property = PropertySerializer()
    days_since_booked = serializers.SerializerMethodField()
    class Meta:
        model = Booking
        fields = '__all__'
    
    def get_days_since_booked(self, obj):
        """Only calculate the days since booked if the status is 'confirmed'."""
        if obj.status == 'confirmed':
            return f"{(date.today() - obj.created_at.date()).days} days"
        return None
        
    
