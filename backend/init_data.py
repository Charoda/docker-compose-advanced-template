# Скрипт заполнения базы тестовыми данными
import time
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from base import SessionLocal, User, engine

# Ждём готовности БД
for attempt in range(10):
    try:
        engine.connect()
        break
    except OperationalError:
        print(f"БД не готова (попытка {attempt + 1}/10), повтор через 2 сек...")
        time.sleep(2)
else:
    raise RuntimeError("Не удалось подключиться к базе данных после 10 попыток.")

# Создаём таблицы
from base import Base
Base.metadata.create_all(bind=engine)

# Тестовые пользователи
users = [
    User(login='pavel', email='a@gmail.com'),
    User(login='yura', email='b@gmail.com'),
]

db: Session = SessionLocal()
try:
    for user in users:
        # Проверяем, нет ли уже такого пользователя
        existing = db.query(User).filter(User.email == user.email).first()
        if not existing:
            db.add(user)
    db.commit()
    print(f"Тестовые данные успешно загружены: {len(users)} пользователей.")
finally:
    db.close()
