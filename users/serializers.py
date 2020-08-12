from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    password_confirm = serializers.CharField(required=True, write_only=True)


    def create(self, validated_data):
        """
        Args:
            validated_data:
        """
        del validated_data["password_confirm"]
        user = User.objects.create_user(**validated_data)

        return user



    def validate(self, attrs):
        """
        Args:
            attrs:
        """
        if User.objects.filter(email=attrs['email']).exists():
            raise ValidationError({'error':{
                    'message': "Email already exists."
                }}
                )
        if attrs["password"] != attrs["password_confirm"]:
            raise ValidationError({'error': {'message': "The two password fields didn't match.",

                                                }}
                                  )


        return attrs