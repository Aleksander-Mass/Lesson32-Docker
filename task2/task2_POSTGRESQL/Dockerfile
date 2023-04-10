# Установка базового образа
FROM python:3.9

# Обновление системных пакетов и установка необходимых для работы PostgreSQL утилит
RUN apt-get update && apt-get install -y postgresql-client

# Копирование файлов проекта в контейнер
COPY . /task2_POSTGRESQL

# Установка зависимостей проекта
RUN pip install -r /task2_POSTGRESQL/requirements.txt

# Установка переменных окружения для базы данных
ENV DATABASE_URL postgresql:myuser:mypassword@localhost:5432/mydatabase

# Инструкция по запуску контейнера
CMD ["python", "/task2_POSTGRESQL/main.py"]
