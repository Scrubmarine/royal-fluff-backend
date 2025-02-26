from django.core.exceptions import ValidationError
from rest_framework import serializers

from api.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        user = CustomUser(**data)
        try:
            user.full_clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)
        return data

    def create(self, validated_data):
        # pop the password from the data, create a user object
        # with the validated data, set the password manually for hashing
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
