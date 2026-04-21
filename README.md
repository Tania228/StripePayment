# Stripe Payment Integration

Django проект с интеграцией Stripe для оплаты товаров и заказов.

## 🚀 Быстрый старт

### Локальный запуск

```bash
1. Клонировать репозиторий
git clone <your-repo-url>
cd Stripe_backend_tz

2. Создать виртуальное окружение
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

3. Установить зависимости
pip install -r requirements.txt

4. Создать .env файл (заполнить своими ключами)
cp .env.example .env

5. Применить миграции
python manage.py migrate

6. Создать суперпользователя
python manage.py createsuperuser

7. Запустить сервер
python manage.py runserver
```

## Docker запуск
```
docker-compose up --build

docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser
```


## API

| URL | Описание |
|-----|----------|
| `/item/{id}/` | Страница товара с кнопкой Buy |
| `/buy/{id}/` | Получить Stripe Session ID |
| `/order/{id}/` | Оплата заказа (несколько товаров) |
| `/admin/` | Панель администратора |


## Тестовая карта Stripe

- **Номер**: `4242 4242 4242 4242`
- **Срок**: любая будущая дата
- **CVC**: любой
