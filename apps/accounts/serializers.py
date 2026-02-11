from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]


class UserWGroupsSerializer(ModelSerializer):
    groups = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "groups"]

    def get_groups(self, obj):
        return [group.name for group in obj.groups.all()]


class UserBasicSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]
