import os
from django.forms import ValidationError
from tattoos.models import Tattoo
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import TattoosSerializer
from .permissions import IsSuperUserOrReadOnly
from Vinilos import settings

class TattoosImgMultiparser(viewsets.ModelViewSet):

    queryset = Tattoo.objects.all()
    serializer_class = TattoosSerializer
    permission_classes = [IsSuperUserOrReadOnly]

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
        
    def destroy(self, request, *args, **kwargs):
        try:
            # Obtén la instancia que se va a eliminar
            instance = self.get_object()

            # Verifica si tiene una foto asociada
            if instance.photo:
                # Obtén la ruta absoluta del archivo
                photo_path = os.path.join(settings.MEDIA_ROOT, str(instance.photo))
                
                # Verifica si el archivo existe y elimínalo
                if os.path.isfile(photo_path):
                    os.remove(photo_path)

            # Elimina la instancia del modelo
            instance.delete()

            return Response(
                {"message": "Tattoo y foto asociados eliminados correctamente"},
                status=status.HTTP_204_NO_CONTENT
            )
        except ValidationError as e:
            return Response({'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error inesperado': f'Intenta again: {e}'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def update(self, request, *args, **kwargs):
        try:
            # Obtén la instancia que se va a eliminar
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)

            if not serializer.is_valid():
                return Response({'messege': f'Hubo un error en las validaciones: {serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)

            data = serializer.validated_data   

            # Verifica si tiene una foto asociada
            if instance.photo and data['photo']:
                # Obtén la ruta absoluta del archivo
                photo_path = os.path.join(settings.MEDIA_ROOT, str(instance.photo))
                
                # Verifica si el archivo existe y elimínalo
                if os.path.isfile(photo_path):
                    os.remove(photo_path)

            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except ValidationError as e:
            return Response({'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error inesperado': f'Intenta again: {e}'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def partial_update(self, request, *args, **kwargs):
        """
        Método para actualizar parcialmente un objeto.
        Solo requiere que se envíen los campos que se quieren actualizar.
        """
        try:
            # Obtén la instancia a actualizar
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)

            if not serializer.is_valid():
                return Response(
                    {'message': f'Hubo un error en las validaciones: {serializer.errors}'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            data = serializer.validated_data   

            # Verifica si tiene una foto asociada
            if instance.photo and data['photo']:
                # Obtén la ruta absoluta del archivo
                photo_path = os.path.join(settings.MEDIA_ROOT, str(instance.photo))
                
                # Verifica si el archivo existe y elimínalo
                if os.path.isfile(photo_path):
                    os.remove(photo_path)

            # Guarda la actualización parcial
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'Error inesperado: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)