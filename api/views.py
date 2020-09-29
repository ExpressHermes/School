from rest_framework import viewsets
from api.models import User
from api.serializers import UserSerializer

# model view set to list all users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
