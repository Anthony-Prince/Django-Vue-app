from django.urls import path

from rest_framework import routers
from .views import EmployeeViewSet

router = routers.DefaultRouter()

router.register('employees', EmployeeViewSet)

urlpatterns = router.urls