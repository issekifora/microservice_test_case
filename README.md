# Microservice template
Boilerplate-проект для создания микросервисов. Содержит весь необходимый обвес для создания полноценного микросервиса по нашим стандартам.

## Организация проекта
* Стандартная структура проекта
* Параметры конфигурации в `config.py`
* Зависимости приложения в`requirements.txt` и зависимости тестирования в `requirements-test.txt`
* Логирование в json с помощью Logging и python-json-logger (подходит для перехватывания логов в ELK)

## API:
* Flask-сервер в development-режиме в `server.py`
* Flask-сервер в production-реживе в `wsgi.py`


## CLI
* Добавлен инструмент командной строки, информация доступна при запуске `python run_reverse_string.py -h` 

## Распределенное выполнение
* Интеграция с RabbitMQ в `consumer.py`

## API и стандарты:
* Спецификация API с помощью OpenAPI 3.0.0 и Swagger UI
* Спецификация сообщений, передаваемых через брокера, с помощью JSON schema по стандарту JSON RPC 2.0

## Тестирование
* Юнит-тесты, функциональные тесты и интеграционные тесты, написанные с помощью `pytest`
* Конфигурация `pytest` в `pytest.ini`
* Автоматический запуск тестов с подготовленным окружением с помощью `tox`, сконфигурированный в `tox.ini`

## CI/CD
* Dockerfile
* Jenkinsfile




