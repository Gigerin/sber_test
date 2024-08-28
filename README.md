# Sber Test

Этот проект представляет собой приложение на Flask для вычисления депозита с использованием Docker. Он использует `pylint` для анализа кода и `pytest` для выполнения тестов с покрытием.

## Требования

- Docker

## Установка и запуск

1. **Клонируйте репозиторий:**

   ```bash
   git clone git@github.com:Gigerin/sber_test.git
2. **Постройте Докер образ**
    ```bash
    docker build -t sber_image .
3. **Запустите контейнер**
    ```bash
   docker run --name sber_test -p 5000:5000 sber_image
