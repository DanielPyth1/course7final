import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from habits.models import Habit
from django.core.exceptions import ValidationError

@pytest.mark.django_db
def test_create_habit():
    user = User.objects.create_user(username="testuser", password="password")
    client = APIClient()
    client.force_authenticate(user=user)

    data = {
        "place": "Дом",
        "time": "08:00:00",
        "action": "Сделать зарядку",
        "is_pleasant": True,
        "periodicity": 1,
        "duration": 30
    }
    response = client.post("/habits/habits/", data, format="json")
    assert response.status_code == 201


@pytest.mark.django_db
def test_get_habits():
    user = User.objects.create_user(username="testuser", password="password")
    Habit.objects.create(
        user=user,
        place="Дом",
        time="08:00:00",
        action="Сделать зарядку",
        is_pleasant=True,
        periodicity=1,
        duration=30
    )
    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get("/habits/habits/")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["action"] == "Сделать зарядку"


@pytest.mark.django_db
def test_habit_model_validation():
    user = User.objects.create_user(username="testuser", password="password")

    habit = Habit(
        user=user,
        place="Дом",
        time="08:00:00",
        action="Сделать зарядку",
        is_pleasant=True,
        periodicity=8,
        duration=60
    )

    with pytest.raises(ValidationError) as excinfo:
        habit.clean()

    assert "Периодичность выполнения должна быть не реже 1 раза в 7 дней." in str(excinfo.value)


@pytest.mark.django_db
def test_access_denied_for_anonymous():
    client = APIClient()
    response = client.get("/habits/habits/")
    assert response.status_code == 401
