from .models import Piercing
from rest_framework import serializers

class PiercingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piercing
        fields = '__all__'
