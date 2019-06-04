from .serializers import DogSerializer
from rest_framework import viewsets
from .models import Dog

class DogViewSet(viewsets.ModelViewSet):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()