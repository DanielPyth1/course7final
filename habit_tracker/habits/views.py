from rest_framework import viewsets, permissions, status
from .models import Habit
from .serializers import HabitSerializer, HabitReminderSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'], permission_classes=[permissions.AllowAny])
    def public(self, request):
        public_habits = Habit.objects.filter(is_public=True)
        serializer = self.get_serializer(public_habits, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        if self.action == 'list':
            return Habit.objects.filter(user=self.request.user)
        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitReminderViewSet(viewsets.ModelViewSet):
    serializer_class = HabitReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if not serializer.validated_data.get('time'):
            serializer.save(user=self.request.user, time="00:00:00")
        else:
            serializer.save(user=self.request.user)


