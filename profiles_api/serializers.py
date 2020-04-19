from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserSerializer(serializers.ModelSerializer):
    """Serializes a User Object"""

    class Meta:
        model = models.User
        fields = ('id', 'email','name', 'password',)
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
        }


    def create(self, validated_data):
        """Create and return a new user"""

        user = models.User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )

        return user



class UserFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    class Meta:
        model = models.UserFeedItem
        fields = ('id', 'user', 'status_text', 'created_on',)
        extra_kwargs = {
            'user': {
                'read_only': True
            }
        }