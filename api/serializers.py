from rest_framework import serializers
from api.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'title')
        extra_kwargs = {'password': {'write_only': True}}

    # create a new user
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    # updating user information including password
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        password = validated_data.get('password')
        instance.set_password(password)
        instance.save()
        return instance
