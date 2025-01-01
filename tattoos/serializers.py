from rest_framework import serializers
from .models import Tattoo

class TattoosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tattoo
        fields = '__all__'

        def validate(self, data):
             if 'photo' not in data:
                raise serializers.ValidationError("Falta la imagen de el tattoo")
             return data