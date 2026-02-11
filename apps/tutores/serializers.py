from rest_framework import serializers
from django.contrib.auth.models import Group, User

from apps.accounts.serializers import UserBasicSerializer, UserSerializer
from apps.tutores import models
from apps.utils import validate_user_with_id


class TutorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Tutor
        fields = ["user", "celular"]


class TutorBasicSerializer(serializers.ModelSerializer):
    user = UserBasicSerializer()

    class Meta:
        model = models.Tutor
        fields = ["user", "celular"]


class TutorCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=False)
    first_name = serializers.CharField(max_length=150, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(max_length=128, required=False)

    user_id = serializers.IntegerField(required=False)
    celular = serializers.CharField(max_length=20, required=False)

    def validate(self, data):
        validate_user_with_id(data)
        user_id = data.get("user_id")

        if user_id:
            try:
                user = User.objects.get(id=user_id)
                if user.groups.filter(name="tutores").exists():
                    raise serializers.ValidationError(
                        {"user_id": "Este usuário já é um tutor"}
                    )
            except User.DoesNotExist:
                raise serializers.ValidationError({"user_id": "Usuário não encontrado"})

        return data

    def create(self, validated_data):
        celular = validated_data.pop("celular")
        user_id = validated_data.pop("user_id", None)

        if user_id:
            user = User.objects.get(id=user_id)
        else:
            user = User.objects.create(**validated_data)

        tutores_group, created = Group.objects.get_or_create(name="tutores")
        user.groups.add(tutores_group)

        tutor = models.Tutor.objects.create(user=user, celular=celular)
        return tutor
