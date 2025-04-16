# Здесь будет API реализация для проекта дневника
import os
import environ

env = environ.Env()
environ.Env.read_env()

from rest_framework import viewsets
from .models import DiaryEntry
from .serializers import DiaryEntrySerializer
from rest_framework.permissions import IsAuthenticated

class DiaryEntryViewSet(viewsets.ModelViewSet):
    queryset = DiaryEntry.objects.all()
    serializer_class = DiaryEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DiaryEntry.objects.filter(user=self.request.user)
