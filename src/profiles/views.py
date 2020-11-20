from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from src.profiles.models import MyUser
from src.profiles.serializers import GetUserSerializer, GetUserPublicSerializer


class PublicUserView(ModelViewSet):
    """ Public user information"""
    queryset = MyUser.objects.all()
    serializer_class = GetUserPublicSerializer
    permission_classes = [permissions.AllowAny]


class UserView(ModelViewSet):
    """ User information """
    serializer_class = GetUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MyUser.objects.filter(id=self.request.user.id)