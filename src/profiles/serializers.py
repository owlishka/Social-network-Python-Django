from rest_framework import serializers
from .models import MyUser


class GetUserSerializer(serializers.ModelSerializer):
    """ Output user information"""
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = MyUser
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )


class GetUserPublicSerializer(serializers.ModelSerializer):
    """ Output user public information """
    class Meta:
        model = MyUser
        exclude = (
            "email",
            "phone",
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )


class UserByFollowerSerializer(serializers.ModelSerializer):
    """ User info for followers"""
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'avatar')
