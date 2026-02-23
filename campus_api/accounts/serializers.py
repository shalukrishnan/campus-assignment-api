from rest_framework import serializers
from .models import Student

class StudentRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = Student
        fields = ['username', 'email', 'password', 'department', 'year']

    def create(self, validated_data):
        return Student.objects.create_user(**validated_data)


        