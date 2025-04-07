from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cryptography.fernet import Fernet
import base64
from django.conf import settings

key = base64.urlsafe_b64encode(settings.SECRET_KEY[:32].encode())
cipher = Fernet(key)

type_choices = [
    ('personal', 'Личное'),
    ('ideas', 'Идеи'),
    ('goals', 'Цели'),
    ('thoughts', 'Мысли'),
]

class Category(models.Model):
    name = models.CharField(max_length=50, choices=type_choices, unique=True)

    def __str__(self):
        return self.get_name_display()

class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content_encrypted = models.BinaryField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)

    def set_content(self, raw_text):
        self.content_encrypted = cipher.encrypt(raw_text.encode())

    def get_content(self):
        return cipher.decrypt(self.content_encrypted).decode()

    def __str__(self):
        return self.title
