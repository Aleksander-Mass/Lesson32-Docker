# Установка базового образа
FROM python:3.9

WORKDIR /task2_SQLITE

# Копирование файлов проекта в контейнер
COPY . /task2_SQLITE

# Установка зависимостей проекта
RUN pip install -r /task2_SQLITE/requirements.txt

# Установка переменной окружения для базы данных
ENV DATABASE_URL sqlite:////task2_SQLITE/vacansies.db

# Инструкция по запуску контейнера
CMD ["python", "/task2_SQLITE/main.py"]

