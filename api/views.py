from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models import User
from api.serializers import UserSerializer

# model view set to list all users
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
