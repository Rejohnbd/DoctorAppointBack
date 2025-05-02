from django.shortcuts import render
from rest_framework import viewsets
from .models import Specialty
from .serializers import SpecialtySerializer

# Create your views here.

class SpecialtyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Specialty.objects.filter(is_published=True).order_by('-created_at')
    serializer_class = SpecialtySerializer
