# Скрипт инициализации БД: создаёт таблицы, дожидаясь готовности PostgreSQL
import time
from sqlalchemy.exc import OperationalError
from base import Base, engine

for attempt in range(10):
    try:
        Base.metadata.create_all(bind=engine)
        print("База данных успешно инициализирована.")
        break
    except OperationalError:
        print(f"БД не готова (попытка {attempt + 1}/10), повтор через 2 сек...")
        time.sleep(2)
else:
    raise RuntimeError("Не удалось подключиться к базе данных после 10 попыток.")