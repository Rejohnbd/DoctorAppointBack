from django.db import models

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=255)
    division = models.ForeignKey('location.Division', on_delete=models.CASCADE)
    district = models.ForeignKey('location.District', on_delete=models.CASCADE)
    thana = models.ForeignKey('location.Thana', on_delete=models.CASCADE, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    help_line = models.CharField(max_length=255, null=True, blank=True)
    help_line2 = models.CharField(max_length=255, null=True, blank=True)
    help_line3 = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name