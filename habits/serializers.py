from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Habit, HabitCompletion

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class HabitCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitCompletion
        fields = ['id', 'date']

class HabitSerializer(serializers.ModelSerializer):
    completed_dates = serializers.SerializerMethodField()

    class Meta:
        model = Habit
        fields = ['id', 'user', 'name', 'description', 'color', 'icon', 'created_at', 'completed_dates']
        read_only_fields = ['user', 'created_at', 'completed_dates']

    def get_completed_dates(self, obj):
        return [completion.date for completion in obj.completions.all()] 