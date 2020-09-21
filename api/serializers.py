from rest_framework import serializers
from .models import Pharacter, MoviePharacter

class PharacterSerializers(serializers.Serializer):
    #table pharacters
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `pharacters` instance, given the validated data.
        """
        return Pharacter.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `pharacters` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance   

class MoviePharacterSerializers(serializers.Serializer):
    #table pharacters
    pk = serializers.IntegerField(read_only=True)
    pharacters_id = serializers.IntegerField()
    movie_id = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `pharacters` instance, given the validated data.
        """
        return MoviePharacter.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `pharacters` instance, given the validated data.
        """
        instance.pharacters = validated_data.get('pharacters', instance.pharacters)
        instance.movie = validated_data.get('movie', instance.movie)
        instance.save()
        return instance             
