# Тестовое задание, компания Ришат

![example workflow](https://github.com/AntonDMoskalev/test_rishat/actions/workflows/main.yml/badge.svg)

### Технологии:

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/) [![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/) [![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/) [![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/) [![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/) [![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/) [![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions) [![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)


## Описание технической части проекта:

#### 1. Реализовано небольшое API с помощью Django (без DRF согласно заданию).

#### 2. Созданы модели: Item, Tax, Discount, Order.

#### 3. В модели Item, учтена валютная корзина (usd, eur), а также Tax для каждого обьекта Item.

#### 4. Все модели импортированы в Панель Администратора, поле Item имеет кастомную форму создания.

#### 5. Для модели Tax, Discount настроена автоматическая регистрация в Stripe с получением ID.

#### 6. Проект реализован на PostgreSQL

#### 7. Запуск через docker-compose, gunicorn, NGINX

#### 8. [Релизован тестовый сервер](http://84.201.153.232/order/2)

#### 9. Настроен GitHub Actions 3 этапа (Проверка PEP8, cборка docker-образа и отправка в Docker Hub, Деплой на сервер)

_______________________________________________________________________________________________________________________________________________________________________

### Тестирование на сервере:

#### Для теста на сервере созданы 8 предметов (Item) с id от 1 до 8.

> [Покупка Item (id=1)](http://84.201.153.232/item/1)

> [Покупка Item (id=6)](http://84.201.153.232/item/6)

>>Эндпоинт для теста: http://84.201.153.232/item/id

>>Получить ключ сессии для Item (Пример Item с ID == 1) http://84.201.153.232/buy/1

#### Для теста на сервере созданы 2 корзины (Order) с id от 1 до 2.

> [Покупка Order (id=1)](http://84.201.153.232/order/1)

> [Покупка Order (id=2)](http://84.201.153.232/order/2)

>>Эндпоинт для теста: http://84.201.153.232/order/id

>>Получить ключ сессии для Order (Пример Item с ID == 1) http://84.201.153.232/order-buy/1

______________________________________________________________________________________________________________________________________________________________________

### Запуск на локально:

> Клонировать репозиторий git clone https://github.com/AntonDMoskalev/test_rishat.git

> Создать файл .env в корне проекта:

#### .env c дефолтными значениями для более легкого тестирования кода:

> SECRET_KEY=django-insecure-m_$c95i)*)y7r=s^0rp$+##8(2@j^7!o_xo1_=+no&co3ud6%8

> STRIPE_SECRET_KEY=sk_test_4eC39HqLyjWDarjtT1zdp7dc

> STRIPE_PUBLISHABLE_KEY=pk_test_TYooMQauvdEDq54NiTphI7jx

> DB_ENGINE=django.db.backends.postgresql

> DB_NAME=postgres

> POSTGRES_USER=postgres

> POSTGRES_PASSWORD=postgres

> DB_HOST=db

> DB_PORT=5432

### Запуск Docker-compose

> docker-compose up -d

### Провести миграции, создать суперпользователя, собрать статику

> docker-compose exec web python manage.py migrate

> docker-compose exec web python manage.py createsuperuser


> docker-compose exec web python manage.py collectstatic --no-input

---
### Контакты:
##### [Linkedin](https://www.linkedin.com/in/anton-dev-py/)
##### [Telegram](https://t.me/MoskalevAD)
##### [GitHub](https://github.com/AntonDMoskalev)
