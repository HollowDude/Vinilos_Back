from .models import Piercing
from rest_framework import serializers

class PiercingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piercing
        fields = '__all__'

        def validate(self, data):
            if 'photo' not in data:
                raise serializers.ValidationError("Falta la imagen del piercing")
            return data