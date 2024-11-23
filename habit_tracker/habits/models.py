from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    place = models.CharField(max_length=255, verbose_name="Место выполнения")
    time = models.TimeField(null=True, blank=True, verbose_name="Время выполнения")
    action = models.CharField(
        max_length=255,
        verbose_name="Действие",
        null=True,
        blank=True)
    is_pleasant = models.BooleanField(default=False, verbose_name="Приятная привычка")
    related_habit = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.SET_NULL, verbose_name="Связанная привычка",
        related_name="related_to"
    )
    periodicity = models.PositiveIntegerField(
        default=1, verbose_name="Периодичность выполнения (в днях)")
    reward = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Вознаграждение")
    duration = models.PositiveIntegerField(
        default=120, verbose_name="Время на выполнение (в секундах)")
    is_public = models.BooleanField(default=False, verbose_name="Публичная привычка")
    reminder_time = models.TimeField(
        null=True, blank=True, verbose_name="Время напоминания")

    def __str__(self):
        return self.action

    def clean(self):
        if self.reward and self.related_habit:
            raise ValidationError(
                "Нельзя указывать и вознаграждение, "
                "и связанную привычку одновременно.")

        if self.duration > 120:
            raise ValidationError("Время на выполнение не должно превышать 120 секунд.")

        if self.related_habit and not self.related_habit.is_pleasant:
            raise ValidationError("Связанная привычка должна быть приятной.")

        if self.is_pleasant and (self.reward or self.related_habit):
            raise ValidationError(
                "Приятная привычка не может иметь вознаграждение "
                "или связанную привычку.")

        if self.periodicity > 7:
            raise ValidationError(
                "Периодичность выполнения должна быть не реже 1 раза в 7 дней.")
