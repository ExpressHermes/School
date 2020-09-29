from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdminUser, IsLoggedInUserOrAdmin

# model view set to list all users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action == 'create':
            permission_classes += [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes += [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes += [IsAdminUser]
        return [permission() for permission in permission_classes]
