from  rest_framework import  serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serialzes a name field for testing our APIView"""

    # like form field like validation + obj to json vice versa

    name =serializers.CharField(max_length=10)

# ModelSerializer helps for existing database
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        #make password field should be write only
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'    #make ******
                }
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name = validated_data['name'],
            password= validated_data['password']
        )
        return user