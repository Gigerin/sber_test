# Sber Test

Этот проект представляет собой приложение на Flask для вычисления депозита с использованием Docker. Он использует `pylint` для анализа кода и `pytest` для выполнения тестов с покрытием.

## Требования

- Docker
- poetry

## Установка и запуск

1. **Клонируйте репозиторий:**

   ```bash
   git clone git@github.com:Gigerin/sber_test.git
   cd sber_test
2. **Установите нужные пакеты**
    ```bash
    make install
3. **Запустите контейнер**
    ```bash
   make build
   make up
Также можно проверить код перед запуском при помощи команд:
   ```bash
   make pylint
   make pytest