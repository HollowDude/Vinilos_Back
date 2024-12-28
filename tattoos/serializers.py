from rest_framework import serializers
from .models import Tattoos

class TattoosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tattoos
        fields = '__all__'