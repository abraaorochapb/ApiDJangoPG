from rest_framework import serializers
from Animes.models import Animes

class AnimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animes
        fields = '__all__'