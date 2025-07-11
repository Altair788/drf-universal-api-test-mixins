# DRF Universal API Test Mixins

[![PyPI version](https://img.shields.io/pypi/v/drf-universal-api-test-mixins.svg)](https://pypi.org/project/drf-universal-api-test-mixins/)
[![PyPI downloads](https://img.shields.io/pypi/dm/drf-universal-api-test-mixins.svg)](https://pypi.org/project/drf-universal-api-test-mixins/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/drf-universal-api-test-mixins.svg)](https://pypi.org/project/drf-universal-api-test-mixins/)
**Универсальные миксины для автоматизации тестирования REST API на Python/Django REST Framework.**

## Описание

Этот пакет содержит три миксина, которые:

- **Сокращают количество ручного кода в тестах**
- **Увеличивают покрытие тестами**
- **Облегчают поддержку тестов при изменениях в проекте**
- **Могут применяться в любом проекте на Django/DRF**

## Основные миксины

1. **CRUDAPITestMixin**  
   Автоматизирует тесты для CRUD-эндпоинтов: проверяет разрешённые/запрещённые HTTP-методы, разрешение URL, аутентификацию, поведение при пустых данных.

2. **ResponseStructureMixin**  
   Проверяет структуру и содержимое ответов API для list/retrieve-запросов.

3. **ValidationErrorTestMixin**  
   Стандартизирует проверку ошибок валидации для POST/PUT/PATCH-запросов.

## Пример использования

```python
from mixins import CRUDAPITestMixin, ResponseStructureMixin
from rest_framework.test import APITestCase


# Предположим, что MyModel — это ваша модель Django:
# from myapp.models import MyModel

class MyModelListView:
    pass


class MyModel:
    pass


class MyModelAPITestCase(CRUDAPITestMixin, ResponseStructureMixin, APITestCase):
    list_url_name = "my-model-list"
    list_view_class = MyModelListView
    allowed_list_methods = ["get"]
    model = MyModel
    expected_item_fields = {"id", "name", "created_at"}

    def setUp(self):
        MyModel.objects.create(name="Test 1")
        MyModel.objects.create(name="Test 2")
```

## Установка

> Пакет можно устанавливать как через Poetry, так и через pip.

### Через Poetry

```bash
poetry add drf-universal-api-test-mixins
```

### Через pip

```bash
pip install drf-universal-api-test-mixins
```

**или напрямую из репозитория:**

```bash
pip install git+https://github.com/Altair788/drf-universal-api-test-mixins.git
```

## Почему это удобно?

- **Миксины универсальны** — подходят для любого DRF-проекта.
- **Минимум кода** — только настройка атрибутов и минимум ручных тестов.
- **Лёгкая поддержка** — изменения в API требуют правки только в одном месте.

**Автор:** Eduard Slobodyanik  
**Telegram:** [@eslobodyanik](https://t.me/eslobodyanik)  
**GitHub:** [Altair788](https://github.com/Altair788)