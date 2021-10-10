
from django.db import router
from django.urls import path, include
from rest_framework import routers
from .views import StudentsViewSet


router = routers.DefaultRouter()
router.register('students', StudentsViewSet)

urlpatterns = router.urls