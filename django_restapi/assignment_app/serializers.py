from rest_framework import serializers
from .models import Hotels


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = ['id','name', 'total_number_of_rooms', 'number_of_rooms_available', 'website_url']