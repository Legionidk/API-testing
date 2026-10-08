import pytest


@pytest.fixture(scope="class")
def shared_posts():
    return [
        {"userId": 1, "id": 0, "title": "Это тестовый пост - 0"},
        {"userId": 1, "id": 1, "title": "Это тестовый пост - 1"},
        {"userId": 1, "id": 2, "title": "Это тестовый пост - 2"},
        {"userId": 2, "id": 3, "title": "Это тестовый пост - 3"},
        {"userId": 3, "id": 4, "title": "Это тестовый пост - 4"},
    ]
