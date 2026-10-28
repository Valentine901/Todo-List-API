from rest_framework import serializers
from .models import User 
from django.contrib.auth import authenticate

# class CreateUserSerializer(serializers.Serializer):
#     email = serializers.EmailField(max_length=200, unique=True, allow_blank=False, required=True)
#     password = serializers.CharField(min_length=8, required=True)

#     def create(self, validated_data):
#         new_user = User.objects.create(**validated_data)
#         return new_user 

# model serializer make code more concised and cool
class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User 
        fields = ["email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user 


    # Incoming JSON from the client
    # {"title": "Clean Code", "author": 3, "price": "29.99", "extra": "ignored"}

    # # serializer.validated_data
    # {
    #     "title": "Clean Code",
    #     "author": <Author: Robert Martin>,   # ID converted to a model instance (if PrimaryKeyRelatedField)
    #     "price": Decimal("29.99"),           # string converted to Decimal
    # }


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=200, min_length=5, required=True, write_only=True)
    password = serializers.CharField(write_only=True, required=True)
    def validate(self, attrs):
        user = authenticate(
            request=self.context.get("request"),
            username=attrs["email"], #type: ignore
            password=attrs["password"], #type: ignore
        )
        if user is None:
            raise serializers.ValidationError("Invalid email or password", 401)
        attrs["user"] = user
        return attrs
    
class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ["id", "email"]
        