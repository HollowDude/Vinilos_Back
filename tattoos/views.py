from django.forms import ValidationError
from tattoos.models import Tattoo
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import TattoosSerializer

class TattoosImgMultiparser(viewsets.ModelViewSet):

    queryset = Tattoo.objects.all()
    serializer_class = TattoosSerializer

    def create(self, request, *args, **kwargs):
        try:

            serializer = TattoosSerializer(data = request.data)

            if not serializer.is_valid():
                return Response({'messege': f'Hubo un error en las validaciones: {serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)

            data = serializer.validated_data           
            tatt = Tattoo(**data)
            tatt.save()
            serializer_response = TattoosSerializer(tatt)

            return Response(serializer_response.data, status = status.HTTP_201_CREATED)
        
        except ValidationError as e:
            return Response({'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'Error inesperado' : f'Intente again: {e}'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)