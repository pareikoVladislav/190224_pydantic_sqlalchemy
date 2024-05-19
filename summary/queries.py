import datetime
from sqlalchemy import func
from typing import Any

from summary.connector import DBConnection
from summary import engine
from summary.models import Role, User, Comment, News

import json


def default_converter(obj: Any) -> str:
    if isinstance(obj, datetime.datetime):  # Проверяем, является ли obj объектом класса datetime.datetime.
        return obj.strftime("%Y-%m-%d %H:%M:%S")  # Если obj является datetime, преобразуем его в строку формата "ГГГГ-ММ-ДД ЧЧ:ММ:СС" и возвращаем эту строку.
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
    # Если obj не является datetime, вызываем исключение TypeError с сообщением о том, что объект данного типа
    # не может быть сериализован в JSON.


# вывести пользоватeля и их комменты
def get_user_info(user_id: int = 8) -> str:
    # Открываем сессию базы данных с использованием контекстного менеджера DBConnection и передаем в него объект engine.
    with DBConnection(engine=engine) as session:
        # Выполняем запрос к базе данных, чтобы получить пользователя с заданным user_id и сохраняем результат в переменную user.
        user: User = session.query(
            User
        ).get(user_id)

        # Создаем словарь user_data для хранения данных о пользователе.
        user_data: dict[str, ...] = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone": user.phone,
            "email": user.email,
            "role_id": "moderator" if user.role_id == 2 else "author",  # Если role_id пользователя равен 2, то устанавливаем значение "moderator", иначе "author".
            "rating": user.rating,
            "created_at": user.created_at,
            "updated_at": user.updated_at,
            "comments": [  # Создаем список комментариев пользователя, каждый комментарий представлен как словарь с id и содержимым.
                {
                    "id": comment.id,
                    "content": comment.content
                }
                for comment in user.comments
            ]
        }
        # Преобразуем словарь user_data в формат JSON с отступами в 4 пробела, используя функцию default_converter для обработки
        # специальных типов данных, и возвращаем результат.
        return json.dumps(user_data, indent=4, default=default_converter)


# обновить рейтинг пользователя
def update_user_rating(user_id: int = 8, rating: float = 8.0) -> str:
    # Открываем сессию базы данных с использованием контекстного менеджера DBConnection и передаем в него объект engine.
    with DBConnection(engine=engine) as session:
        # Выполняем запрос к базе данных, чтобы получить пользователя с заданным user_id и сохраняем результат в переменную user.
        user: User = session.query(
            User
        ).get(user_id)

        user.rating = rating  # Обновляем рейтинг пользователя на переданное значение rating.
        session.commit()  # Фиксируем изменения в базе данных.

        # Создаем словарь user_data для хранения данных о пользователе.
        user_data: dict[str, ...] = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone": user.phone,
            "email": user.email,
            "role_id": "moderator" if user.role_id == 2 else "author",
            "rating": user.rating,
            "created_at": user.created_at,
            "updated_at": user.updated_at,
            "comments": [
                {
                    "id": comment.id,
                    "content": comment.content
                }
                for comment in user.comments
            ]
        }

        # Преобразуем словарь user_data в формат JSON с отступами в 4 пробела, используя функцию default_converter для обработки
        # специальных типов данных, и возвращаем результат.
        return json.dumps(user_data, indent=4, default=default_converter)


# получить самую последнюю новость юзера
def get_latest_user_news(user_id: int = 8) -> str:
    # Открываем сессию базы данных с использованием контекстного менеджера DBConnection и передаем в него объект engine.
    with DBConnection(engine=engine) as session:
        # Выполняем запрос к базе данных для получения последней новости, созданной пользователем с заданным user_id.
        user_last_news: News = session.query(News).filter(
            News.author_id == user_id  # Фильтруем записи по author_id,
        ).order_by(News.created_at.desc()).first()# сортируем их по дате создания в порядке убывания и выбираем первую запись.

        user_data: dict[str, ...] = {
            # Создаем словарь user_data для хранения данных о последней новости пользователя.
            "id": user_last_news.id,
            "title": user_last_news.title,
            "content": user_last_news.content,
            "user_info": {
                "first_name": user_last_news.user.first_name,
                "email": user_last_news.user.email,
                "rating": user_last_news.user.rating,
            }

        }
        # Преобразуем словарь user_data в формат JSON с отступами в 4 пробела и возвращаем результат.
        return json.dumps(user_data, indent=4)


# посчитать кол-во пользователей по рейтингу
def count_users_by_rating() -> str:
    # Открываем сессию базы данных с использованием контекстного менеджера DBConnection и передаем в него объект engine.
    with DBConnection(engine=engine) as session:
        # Выполняем запрос к базе данных для получения рейтинга пользователей и количества пользователей с каждым рейтингом.
        users: list[User, ...] = session.query(
            User.rating,
            func.count(User.id).label('count_of_users')  # получаем кол-во пользователей
        ).group_by(User.rating).all()  # Группируем результаты по полю rating и подсчитываем количество пользователей (count_of_users) для каждого рейтинга.

        # Создаем список словарей users_data, где каждый словарь содержит рейтинг пользователя и количество пользователей с этим рейтингом.
        users_data: list[dict[str, ...]] = [
            {
                "rating": user.rating,
                "count_of_users": user.count_of_users
            }
            for user in users
        ]

        # Преобразуем список users_data в формат JSON с отступами в 4 пробела и возвращаем результат.
        return json.dumps(users_data, indent=4)


# посчитать кол-во новостей для каждого пользователя
def count_news_for_user() -> str:
    # Открываем сессию базы данных с использованием контекстного менеджера DBConnection и передаем в него объект engine.
    with DBConnection(engine=engine) as session:
        # Выполняем запрос к базе данных для получения author_id и количества новостей, созданных каждым автором.
        news: list[News, ...] = session.query(
            News.author_id,
            func.count(News.id).label('count_of_news')  # подсчитываем количество новостей
        ).group_by(News.author_id).all()  # Группируем результаты по полю author_id и подсчитываем количество новостей (count_of_news) для каждого автора.

        # Создаем список словарей news_data, где каждый словарь содержит id автора (author_id) и количество новостей (count_of_news), созданных этим автором.
        news_data: list[dict[str, ...]] = [
            {
                "author_id": obj.author_id,
                "count_of_news": obj.count_of_news
            }
            for obj in news
        ]

        # Преобразуем список news_data в формат JSON с отступами в 4 пробела и возвращаем результат.
        return json.dumps(news_data, indent=4)


# получить пользователей, отсортированных по ролям, исключить администраторов
def get_users_sorted_by_roles() -> str:
    # Открываем сессию базы данных с использованием контекстного менеджера DBConnection и передаем в него объект engine.
    with DBConnection(engine=engine) as session:
        # Выполняем запрос к базе данных для получения
        users: list[User, ...] = session.query(
            User.role_id,  # роли пользователей (role_id)
            func.count(User.id).label('count_of_users')  # и количества пользователей с каждой ролью (count_of_users).
        ).group_by(User.role_id).having(User.role_id != 1).all()  # Группируем результаты по полю role_id, исключая пользователей с ролью role_id = 1, и сохраняем результаты в переменную users.

        # Создаем список словарей users_data, где каждый словарь содержит роль пользователя (role) и количество пользователей с этой ролью (count_of_users).
        users_data: list[dict[str, ...]] = [
            {
                "role": "moderator" if user.role_id == 2 else "author",
                "count_of_users": user.count_of_users
            }
            for user in users
        ]

        # Преобразуем список users_data в формат JSON с отступами в 4 пробела и возвращаем результат.
        return json.dumps(users_data, indent=4)


# получить пользователей, которые написали более 4 новостей
def get_users_by_count_news(count_news: int = 4) -> str:
    # Открываем сессию базы данных с использованием контекстного менеджера DBConnection и передаем в него объект engine.
    with DBConnection(engine=engine) as session:
        # Выполняем подзапрос к базе данных для получения
        news_count_subquery = session.query(
            News.author_id,  # author_id
            func.count(News.id).label('count_of_news')  # и количества новостей (count_of_news), созданных каждым автором
        ).group_by(News.author_id).subquery()  # группируя результаты по полю author_id


        # Выполняем основной запрос к базе данных для получения пользователей,
        # у которых количество новостей больше count_news.
        users: list[User, ...] = session.query(User).join(
            news_count_subquery,  # # Присоединяем подзапрос news_count_subquery
            User.id == news_count_subquery.c.author_id  # по условию совпадения id пользователя и author_id,
        ).filter(news_count_subquery.c.count_of_news > count_news).all()  # фильтруем результаты по количеству новостей.

        users_data: list[dict[str, ...]] = [  # # Создаем список словарей users_data, где каждый словарь содержит информацию о пользователе и его новостях.
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone": user.phone,
                "email": user.email,
                "role_id": user.role_id,
                "rating": user.rating,
                "deleted": user.deleted,
                "created_at": user.created_at,
                "updated_at": user.updated_at,
                "news": [  # Создаем список новостей пользователя,
                    {
                        "id": n.id,
                        "title": n.title,
                        "content": n.content,
                        "moderated": n.moderated,
                        "created_at": n.created_at,
                    }
                    for n in user.news
                ]
            }
            for user in users
        ]

        # Преобразуем список users_data в формат JSON с отступами в 4 пробела, используя функцию default_converter для обработки
        # специальных типов данных, и возвращаем результат.
        return json.dumps(users_data, indent=4, default=default_converter)


# получить пользователей, у которых кол-во новостей больше среднего кол-ва новостей
def get_users_by_news_more_than_mean() -> str:
    # Открываем сессию базы данных с использованием контекстного менеджера DBConnection и передаем в него объект engine.
    with DBConnection(engine=engine) as session:
        # Выполняем подзапрос
        # Группируем результаты по id пользователя и сохраняем подзапрос в переменную subquery.
        subquery = (
            session.query(func.count(News.id).label('count_of_news'))  # для подсчета количества новостей
            .join(User, User.id == News.author_id)
            .group_by(User.id)  # Группируем результаты по id пользователя
            .subquery()
        )

        avg_news_subquery = (
            session.query(func.avg(subquery.c.count_of_news).label('avg_news'))
            .select_from(
                session.query(func.count(News.id).label('news_count'))
                .join(User, User.id == News.author_id)
                .group_by(User.id)
                .subquery()
            )
        ).scalar_subquery()

        news_users: list[User, ...] = session.query(User).join(
            News
        ).group_by(User.id).having(func.count(News.id) > avg_news_subquery).all()

        users_data: list[dict[str, ...]] = [
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "created_at": user.created_at,
                "news": [
                    {
                        "id": n.id,
                        "title": n.title,
                        "content": n.content
                    }
                    for n in user.news
                ]
            }
            for user in news_users
        ]

        return json.dumps(users_data, indent=4, default=default_converter)
