from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from .views import HabitViewSet, HabitReminderViewSet

# Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Habits Tracker API",
        default_version='v1',
        description="Документация API для трекера привычек",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habit')
router.register(r'reminders', HabitReminderViewSet, basename='habit-reminder')

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),
]
