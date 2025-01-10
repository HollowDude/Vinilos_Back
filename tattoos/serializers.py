from rest_framework import serializers
from .models import Tattoo

class TattoosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tattoo
        fields = '__all__'

        def validate(self, data):
             request  = self.context.get('request')
             if request and request.method == "POST":
                if "photo" not in data:
                    raise serializers.ValidationError("Falta la imagen de el tattoo")
             return data
        
        def to_representation(self, instance):
            representation = super().to_representation(instance)
            # Construye la URL completa para el campo photo
            request = self.context.get('request')
            if instance.photo and request:
                representation['photo'] = request.build_absolute_uri(instance.photo.url)
            return representation