from rest_framework import serializers
from .models import Assignment


from django.contrib.auth.models import User
from rest_framework import serializers

class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'subject', 'status', 'created_at']
        read_only_fields = ['created_at']


