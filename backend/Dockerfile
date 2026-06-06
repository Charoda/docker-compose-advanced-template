# Базовый образ — лёгкий Python 3.11
FROM python:3.11-slim

WORKDIR /app

# Сначала копируем только зависимости — это позволит Docker кэшировать слой с pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код приложения
COPY . .

# При старте инициализируем БД и запускаем uvicorn
CMD ["sh", "-c", "python init_db.py && uvicorn main:app --host 0.0.0.0 --port 8000"]
