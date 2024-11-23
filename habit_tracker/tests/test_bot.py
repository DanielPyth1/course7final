import pytest
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from telegram import Update, Message
from telegram.ext import ContextTypes
from unittest.mock import AsyncMock
import uuid
from habits.models import Habit


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_addhabit_command():
    username = f"testuser_{uuid.uuid4().hex[:8]}"
    user = await sync_to_async(User.objects.create_user)(username=username, password="password")

    update = AsyncMock(spec=Update)
    update.message = AsyncMock(spec=Message)
    update.message.text = "/addhabit Сделать зарядку"
    update.message.reply_text = AsyncMock()
    update.effective_user = user
    context = AsyncMock(spec=ContextTypes.DEFAULT_TYPE)
    context.args = ["Сделать", "зарядку"]

    from telegram_bot.bot import add_habit
    await add_habit(update, context)

    update.message.reply_text.assert_called_once_with(
        "Привычка 'Сделать зарядку' успешно добавлена!")


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_addhabit_command():
    username = f"testuser_{uuid.uuid4().hex[:8]}"
    user = await sync_to_async(User.objects.create_user)(username=username, password="password")

    update = AsyncMock(spec=Update)
    update.message = AsyncMock(spec=Message)
    update.message.text = "/addhabit Сделать зарядку"
    update.message.reply_text = AsyncMock()
    update.effective_user = user
    context = AsyncMock(spec=ContextTypes.DEFAULT_TYPE)
    context.args = ["Сделать", "зарядку"]

    from telegram_bot.bot import add_habit
    await add_habit(update, context)

    update.message.reply_text.assert_called_once_with(
        "Привычка 'Сделать зарядку' успешно добавлена!")


@pytest.mark.asyncio
async def test_remind_command():
    from telegram_bot.bot import remind

    update = AsyncMock(spec=Update)
    update.message = AsyncMock(spec=Message)
    update.message.text = "/remind Сделать зарядку"
    update.message.reply_text = AsyncMock()
    context = AsyncMock(spec=ContextTypes.DEFAULT_TYPE)
    context.args = ["Сделать", "зарядку"]

    await remind(update, context)

    update.message.reply_text.assert_called_once_with("Напоминаю: Сделать зарядку")
