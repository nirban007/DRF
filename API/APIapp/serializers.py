from rest_framework import serializers
from APIapp.models import Person

class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=20)
    address = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Person.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance