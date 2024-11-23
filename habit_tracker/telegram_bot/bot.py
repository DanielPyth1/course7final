import os
import sys
import django
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from asgiref.sync import sync_to_async

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'habit_tracker.settings')
django.setup()

from habits.models import Habit

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот для напоминаний о твоих привычках.")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Твой chat_id: {update.effective_chat.id}")


async def add_habit(update, context):
    habit = await sync_to_async(Habit.objects.create)(
        user=update.effective_user,
        action="Сделать зарядку",
        time="08:00:00",
        periodicity=1,
        duration=30,
    )
    await update.message.reply_text(f"Привычка '{habit.action}' успешно добавлена!")


async def list_habits(update: Update, context: ContextTypes.DEFAULT_TYPE):
    habits = Habit.objects.all()
    if habits.exists():
        text = "\n".join([f"- {habit.action}" for habit in habits])
        await update.message.reply_text(f"Ваши привычки:\n{text}")
    else:
        await update.message.reply_text("У вас пока нет привычек.")


async def remind(update, context):
    action = " ".join(context.args)
    await update.message.reply_text(f"Напоминаю: {action}")


if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(CommandHandler("addhabit", add_habit))
    app.add_handler(CommandHandler("listhabits", list_habits))

    print("Бот запущен...")
    app.run_polling()
