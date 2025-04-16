from django.contrib import admin
from django.urls import path, include
from diary import views as diary_views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from diary.api import DiaryEntryViewSet

router = DefaultRouter()
router.register(r'api/entries', DiaryEntryViewSet, basename='entry')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', diary_views.index_view, name='index'),
    path('add/', diary_views.add_entry_view, name='add_entry'),
    path('register/', diary_views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='diary/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + router.urls
