from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.viewsets import ModelViewSet

from students.models import Student
from students.serializers import StudentSerializer

class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer