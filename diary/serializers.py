from rest_framework import serializers, viewsets, permissions
from .models import DiaryEntry

class DiaryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryEntry
        fields = '__all__'
        read_only_fields = ['user']

class DiaryEntryViewSet(viewsets.ModelViewSet):
    serializer_class = DiaryEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DiaryEntry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
