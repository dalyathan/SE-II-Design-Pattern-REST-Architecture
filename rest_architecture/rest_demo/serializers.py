from rest_framework import serializers
from models import Person
class PersonSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=250)
    last_name = serializers.CharField(max_length=250)
    age= serializers.IntegerField(read_only=True)
    def create(self,validated_data):
        return Person.objects.create(**validated_data);
