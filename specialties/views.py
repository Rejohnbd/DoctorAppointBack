from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.core.cache import cache
from .models import Specialty
from .serializers import SpecialtySerializer
from core.utils import custom_response  # Import our custom response

class SpecialtyViewSet(viewsets.ModelViewSet):
    serializer_class = SpecialtySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        cache_key = 'published_specialties'
        queryset = cache.get(cache_key)
        
        if not queryset:
            queryset = Specialty.objects.filter(is_published=True).select_related()
            cache.set(cache_key, queryset, timeout=60*15)
        
        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return custom_response(
            message="All specialties retrieved successfully",
            data=serializer.data
        )

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return custom_response(
    #         message="Specialty details retrieved",
    #         data=serializer.data
    #     )

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
        
    #     cache.delete('published_specialties')
        
    #     return custom_response(
    #         message="Specialty created successfully",
    #         data=serializer.data,
    #         status_code=status.HTTP_201_CREATED
    #     )

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
        
    #     cache.delete('published_specialties')
        
    #     return custom_response(
    #         message="Specialty updated successfully",
    #         data=serializer.data
    #     )

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     cache.delete('published_specialties')
    #     return custom_response(
    #         message="Specialty deleted successfully",
    #         status_code=status.HTTP_204_NO_CONTENT
    #     )

    # @action(detail=False, methods=['get'])
    # def featured(self, request):
    #     featured_specialties = cache.get('featured_specialties')
        
    #     if not featured_specialties:
    #         featured_specialties = self.get_queryset().filter(is_featured=True)
    #         cache.set('featured_specialties', featured_specialties, timeout=60*60)
        
    #     serializer = self.get_serializer(featured_specialties, many=True)
    #     return custom_response(
    #         message="Featured specialties retrieved",
    #         data=serializer.data
    #     )