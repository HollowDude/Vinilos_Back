import os
from django.forms import ValidationError
from piercings.serializers import PiercingsSerializer
from rest_framework.response import Response
from piercings.models import Piercing
from piercings.permissions import IsSuperUserOrReadOnly
from rest_framework import viewsets, status
from Vinilos import settings

class PiercingsImgMultiparser(viewsets.ModelViewSet):
    
    queryset = Piercing.objects.all()
    serializer_class = PiercingsSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    

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
                {"message": "Piercing y foto asociados eliminados correctamente"},
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