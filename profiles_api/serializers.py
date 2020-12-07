from  rest_framework import  serializers

class HelloSerializer(serializers.Serializer):
    """Serialzes a name field for testing our APIView"""

    # like form field like validation + obj to json vice versa

    name =serializers.CharField(max_length=10)
