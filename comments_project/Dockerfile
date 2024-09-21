# 1. Встановлюємо базовий образ для Python
FROM python:3.12

# 2. Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# 3. Копіюємо файл requirements.txt у контейнер
COPY requirements.txt /app/

# 4. Встановлюємо всі залежності з requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копіюємо весь проєкт у контейнер
COPY . /app/

# 6. Налаштовуємо змінні середовища
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=comments_project.settings

# 7. Збираємо статичні файли
RUN python3 manage.py collectstatic --noinput

# 8. Виконуємо міграції бази даних
RUN python3 manage.py migrate

# 9. Вказуємо команду для запуску Django-сервера
CMD ["python", "manage.py", "runserver"]
