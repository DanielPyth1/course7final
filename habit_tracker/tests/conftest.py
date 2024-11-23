import pytest
from django.contrib.auth.models import User

@pytest.fixture(autouse=True)
def clear_database(db):
    User.objects.all().delete()
