from sqlalchemy import func
from sqlalchemy.orm import aliased

from alchemy_queries.connector import DBConnector
from alchemy_queries import engine

from alchemy_queries.models import User


with DBConnector(engine=engine) as session:
    # users = session.query(
    #     User.name,
    #     func.sum(User.age)
    # ).group_by(User.name)
    #
    # print(users)
    #
    # print(users.all())
    #
    # if users:
    #     for user_name, sum_of_age in users:
    #         print(f"Users with name: {user_name}   |   Users sum age: {sum_of_age}")
    #
    # else:
    #     print("NOT FOUND")

    # users = session.query(
    #     User.age,
    #     func.count(User.id)
    # ).group_by(User.age)
    #
    # print(users)
    #
    # print(users.all())
    #
    # if users:
    #     for user_age, count_of_users in users:
    #         print(f"User age: {user_age}   |   Count of users: {count_of_users}")
    #
    # else:
    #     print("NOT FOUND")

    # users = session.query(func.count(User.id)).scalar()
    # users = session.query(func.avg(User.age)).scalar()
    #
    # print(f"Count of users: {users}")
    # print(f"Mean age of users: {users}")

    # my_users = aliased(User, name='my_users')
    #
    # users = session.query(
    #     my_users.age,
    #     func.count(my_users.id).label('count_of_users')
    # ).group_by(my_users.age)
    #
    # print(users)

    # if users:
    #     for user_age, count_of_users in users:
    #         print(f"User age: {user_age}   |   Count of users: {count_of_users}")
    #
    # else:
    #     print("NOT FOUND")

    # print(users.all())
    # if users:
    #     for user in users:
    #         print(f"User age: {user.age}   |   Count of users: {user.count_of_users}")
    #
    # else:
    #     print("NOT FOUND")

    # users = session.query(
    #     User.age,
    #     func.count(User.id).label('count_of_users')
    # ).group_by(User.age).having(func.count(User.id) > 1)
    #
    # print(users)
    #
    # print(users.all())
    #
    # if users:
    #     for user in users:
    #         print(f"User age: {user.age}   |   Count of users: {user.count_of_users}")
    #
    # else:
    #     print("NOT FOUND")

    # sub_query = session.query(
    #     func.avg(User.age).label('mean_age')
    # ).subquery()
    #
    # core_query = session.query(User).filter(
    #     User.age > sub_query
    # )
    #
    # print(session.query(sub_query).scalar())
    #
    # print(core_query)
    #
    # print(core_query.all())
    #
    # if core_query:
    #     for user in core_query:
    #         print(f"User age: {user.age}   |  User name {user.name}")
    #
    # else:
    #     print("NOT FOUND")

    sub_query = session.query(User.name).filter(User.name.like('J%')).subquery()

    core_query = session.query(User).filter(
        User.name.in_(sub_query)
    )

    print(core_query)

    print(core_query.all())

    if core_query:
        for user in core_query:
            print(f"User age: {user.age}   |  User name {user.name}")

    else:
        print("NOT FOUND")