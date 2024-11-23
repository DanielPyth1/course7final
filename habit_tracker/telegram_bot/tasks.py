from celery import shared_task
from telegram import Bot
from datetime import datetime
import os
from habits.models import Habit


@shared_task
def send_reminder(chat_id, habit):
    """Отправка напоминания о привычке через Telegram."""
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=habit)


@shared_task
def send_habit_reminders():
    """Автоматическая отправка напоминаний для всех пользователей с учётом времени."""
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    bot = Bot(token=bot_token)
    now = datetime.now().time()

    habits = Habit.objects.filter(reminder_time__hour=now.hour, reminder_time__minute=now.minute)

    for habit in habits:
        if hasattr(habit.user, 'chat_id') and habit.user.chat_id:
            bot.send_message(
                chat_id=habit.user.chat_id,
                text=f"Напоминание: {habit.action}"
            )
