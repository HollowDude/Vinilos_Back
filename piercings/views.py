from django.forms import ValidationError
from piercings.serializers import PiercingsSerializer
from rest_framework.response import Response
from piercings.models import Piercing
from rest_framework import viewsets, status

class PiercingsImgMultiparser(viewsets.ModelViewSet):
    
    queryset = Piercing.objects.all()
    serializer_class = PiercingsSerializer

    def create(self, request, *args, **kwargs):
        try:

            serializer = PiercingsSerializer(data = request.data)

            if not serializer.is_valid():
                return Response({'message': f'Hubo un error en la validacion:{serializer.errors}'}, status = status.HTTP_400_BAD_REQUEST)

            data = serializer.validated_data
            pierc = Piercing(**data)
            pierc.save()
            serializer_response = PiercingsSerializer(pierc)

            return Response(serializer_response.data, status = status.HTTP_201_CREATED)
        
        except ValidationError as e:
            return Response({'error' : str(e)}, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'Un error inesperado a ocurrido {e}'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)