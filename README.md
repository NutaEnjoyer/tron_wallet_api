# Tron Wallet API

**Tron Wallet API** — сервис для получения информации о кошельках Tron, включая баланс, bandwidth, energy, с сохранением истории запросов в PostgreSQL. Асинхронная работа, автодокументация, контейнеризация.

---

## 🚀 Возможности

- Получение баланса, bandwidth и energy по адресу Tron
- Сохранение истории запросов в PostgreSQL
- Асинхронная работа (FastAPI, SQLAlchemy, tronpy)
- Автогенерируемая документация (Swagger/OpenAPI)
- Контейнеризация (Docker, docker-compose)
- Unit- и интеграционные тесты

---

## 🗂️ Структура проекта

```
app/
├── api/                # Роуты FastAPI
├── core/               # Конфиги, интеграции
├── models/             # SQLAlchemy-модели
├── schemas/            # Pydantic-схемы
├── services/           # Бизнес-логика
├── tron_grid/          # Работа с TronGrid API
├── app.py              # Точка входа FastAPI
Dockerfile
requirements.txt
.env
README.md
docker-compose.yml
tests/                 # Тесты (или test_*.py в корне)
```

---

## ⚙️ Быстрый старт

### 1. Клонируйте репозиторий

```sh
git clone <your-repo-url>
cd tron-wallet-api
```

### 2. Заполните `.env`

Пример:
```
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/testinfourhours
TRONGRID_API_KEY=ваш_ключ
```

### 3. Запустите сервисы

```sh
docker-compose up --build
```

- FastAPI: http://localhost:8000
- Swagger UI: http://localhost:8000/docs

---

## 🧪 Тестирование

```sh
pip install -r requirements.txt
pytest
```

---

## 📝 Примеры запросов

**Получить информацию о кошельке и сохранить в историю:**
```http
POST /api/wallets
{
  "wallet_address": "TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn"
}
```
**Ответ:**
```json
{
  "balance": 4035.754441,
  "bandwidth": 600,
  "energy": 180000000000
}
```

**Получить историю запросов (с пагинацией):**
```http
GET /api/wallets?skip=0&limit=10
```
**Ответ:**
```json
[
  {
    "id": 1,
    "address": "TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn",
    "balance": 4035.754441,
    "bandwidth": 600,
    "energy": 180000000000
  },
  ...
]
```

---

## 📦 Миграции БД

Если используете Alembic:
```sh
alembic revision --autogenerate -m "Комментарий"
alembic upgrade head
```

---

## 📝 Переменные окружения

- `DATABASE_URL` — строка подключения к Postgres
- `TRONGRID_API_KEY` — API-ключ TronGrid

---

## 🛠️ Зависимости

- FastAPI
- SQLAlchemy
- asyncpg
- tronpy[async]
- pydantic
- httpx
- pytest, pytest-asyncio
- Docker, docker-compose

---

## 📄 Лицензия

MIT (или ваша лицензия)