from rest_framework import generics, permissions
from .serializers import StudentRegistrationSerializer
from .models import Student

# class RegisterView(generics.CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentRegistrationSerializer
#     permission_classes = [permissions.AllowAny]


class RegisterView(generics.ListCreateAPIView): # Allows GET and POST
    queryset = Student.objects.all()
    serializer_class = StudentRegistrationSerializer
    permission_classes = [permissions.AllowAny]    