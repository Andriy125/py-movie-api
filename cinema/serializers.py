from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    duration = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance
