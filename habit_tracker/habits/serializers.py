from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = [
            'id', 'user', 'place', 'time', 'action', 'is_pleasant', 'related_habit',
            'periodicity', 'reward', 'duration', 'is_public'
        ]
        read_only_fields = ['user']

    def validate(self, data):
        if data.get('reward') and data.get('related_habit'):
            raise serializers.ValidationError("Нельзя указывать и вознаграждение, и связанную привычку одновременно.")

        if data.get('duration') and data['duration'] > 120:
            raise serializers.ValidationError("Время на выполнение не должно превышать 120 секунд.")

        if data.get('related_habit') and not data['related_habit'].is_pleasant:
            raise serializers.ValidationError("Связанная привычка должна быть приятной.")

        if data.get('is_pleasant') and (data.get('reward') or data.get('related_habit')):
            raise serializers.ValidationError("Приятная привычка не может иметь вознаграждение или связанную привычку.")

        if data.get('periodicity') and data['periodicity'] > 7:
            raise serializers.ValidationError("Периодичность выполнения должна быть не реже 1 раза в 7 дней.")

        return data

class HabitReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'action', 'reminder_time', 'time']
