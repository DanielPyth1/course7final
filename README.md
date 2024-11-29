Курсовая 7. DRF

Выполнил Жиров Даниил

# Habit Tracker Project

## Описание проекта

**Habit Tracker** — это приложение для управления привычками, 
разработанное с использованием Django и Django REST Framework. 
Оно позволяет пользователям добавлять, отслеживать и удалять привычки. 
Проект также включает Telegram-бота для взаимодействия с пользователями через чат, 
предлагая основные команды для управления привычками.

## Возможности
- Регистрация и аутентификация пользователей.
- Создание, редактирование и удаление привычек.
- Управление расписанием привычек (время, периодичность, длительность).
- Telegram-бот для выполнения команд:
  - Добавление привычки.
  - Просмотр списка привычек.
  - Напоминания о привычках.
- Тесты с покрытием 86% с использованием `pytest`.
- Настройка CORS для работы с фронтендом.
- API-документация, созданная с помощью `drf-yasg`.

## Технологии
- **Backend:** Django, Django REST Framework.
- **Telegram Bot:** python-telegram-bot.
- **Тестирование:** Pytest, Pytest-Django, Pytest-Cov.
- **Стиль кода:** flake8.
- **База данных:** PostgreSQL.
- **Развёртывание:** nginx.

## Запуск проекта в Docker

1. Убедитесь, что у вас установлен Docker и Docker Compose.
2. Соберите контейнеры:
   ```bash
   docker-compose up
   docker-compose build

Работа с приложением:
Адрес приложения - http://127.0.0.1:8000

Зайти в админ-панель http://127.0.0.1:8000/admin
