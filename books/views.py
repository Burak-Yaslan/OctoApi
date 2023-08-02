from rest_framework.response import Response
from .models import book
from .serializer import bookSerializer
from rest_framework import viewsets

#viewsets.ModelViewSet
class bookViewSet(viewsets.ModelViewSet):
        queryset = book.objects.all()
        serializer_class = bookSerializer
        

    