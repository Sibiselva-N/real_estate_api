from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        fields = '__all__'


class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EstateModel
        fields = '__all__'
        depth = 1
