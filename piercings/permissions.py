from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSuperUserOrReadOnly(BasePermission):
    """
    Permiso personalizado que permite solo a superusuarios editar, borrar y crear.
    Los usuarios no autenticados o no superusuarios solo pueden hacer GET.
    """

    def has_permission(self, request, view):
        # Métodos seguros (GET, HEAD, OPTIONS) siempre están permitidos
        if request.method in SAFE_METHODS:
            return True
        
        # Otros métodos (POST, PUT, PATCH, DELETE) solo para superusuarios
        return request.user and request.user.is_superuser