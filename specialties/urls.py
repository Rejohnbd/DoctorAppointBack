from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpecialtyViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'specialties', SpecialtyViewSet, basename='specialty')

urlpatterns = [
    path('', include(router.urls)),
]
