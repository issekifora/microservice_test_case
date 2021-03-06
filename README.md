# Вложенный палиндром
Сервис, анализирующий строку и определяющий, содержит ли строка палиндром. Используется для тестовых заданий.

## Организация проекта
* Стандартная структура проекта
* Параметры конфигурации в `config.py`
* Зависимости приложения в`requirements.txt` и зависимости тестирования в `requirements-test.txt`
* Логирование в json с помощью Logging и python-json-logger (подходит для перехватывания логов в ELK)

## API
Проект использует Python 3.6 и старше.

## API
* Flask-сервер в development-режиме в `server.py`
* Flask-сервер в production-режиме в `wsgi.py`

Запуск API осуществляется в подготовленном python-окружении с зависимостями, указанными в requirements.txt.

Запуск dev-версии:

```bash
python server.py
```
После запуска по адресу http://127.0.0.1:10000/template/v0.1/ui/ будет доступен интерфейс Swagger.

Запуск prod-версии
```bash
flask run

```
или
```bash
python wsgi.py
```
После запуска по адресу http://127.0.0.1:5000/template/v0.1/ui/ будет доступен интерфейс Swagger.

## CLI
* Добавлен инструмент командной строки, информация доступна при запуске `python run_is_palindrome.py -h` 

## API и стандарты:
* Спецификация API с помощью OpenAPI 3.0.0 и Swagger UI

## Тестирование
* Юнит-тесты, функциональные тесты и интеграционные тесты, написанные с помощью `pytest`
* Конфигурация `pytest` в `pytest.ini`
* Автоматический запуск тестов с подготовленным окружением с помощью `tox`, сконфигурированный в `tox.ini`

