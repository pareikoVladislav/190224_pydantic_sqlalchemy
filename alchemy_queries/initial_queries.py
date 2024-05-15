import random

from sqlalchemy import and_, or_, not_, desc

from alchemy_queries.connector import DBConnector
from alchemy_queries import engine

from alchemy_queries.models import User

# with DBConnector(engine=engine) as session:
    # user: User = session.query(User).filter(User.id == 5).one()
    # user: User = session.query(User).filter_by(id=5).one()
    # user: User = session.query(User).filter_by(id=999).one()
    # users: list[User, ...] = session.query(User).filter(User.name.startswith("QWERTY")).all()
    # if users:
    #     for user in users:
    #         print(f"{user.id} | {user.name} | {user.age}")
    #
    # else:
    #     print(users)
    #     print("NOT FOUND")

    # user: User = session.query(User).filter_by(id=999).one_or_none()
    # user: User = session.query(User).filter(User.name.startswith("J")).one_or_none()
    # user: User = session.query(User).filter(User.id == 999).one_or_none()

    # print(user)

    # if user is not None:
    #     print(f"{user.id} | {user.name} | {user.age}")
    #
    # else:
    #     print(user)
    #     print("NOT FOUND")

    # users = session.query(User).filter(User.age > 75).all()
    #
    # if users:
    #     for user in users:
    #         print(f"{user.id} | {user.name} | {user.age}")
    #
    # else:
    #     print(users)
    #     print("NOT FOUND")

    # user = session.query(User).filter(User.age > 100).first()
    #
    # if user:
    #     print(f"{user.id} | {user.name} | {user.age}")
    #
    # else:
    #     print(user)
    #     print("NOT FOUND")


# one()
# one_or_none()
# all()
# first()

# ============================================================================================

# FILTRATION
with DBConnector(engine=engine) as session:
    # users = session.query(User).filter(User.name.like('A%'))
    #
    # print(users)
    #
    # if users:
    #     for user in users:
    #         print(f"User ID - {user.id}   |   User name: {user.name}")
    #
    # else:
    #     print("NOT FOUND")

    # names = ['Katie', 'James', 'Thomas', 'Cynthia']
    #
    # users = session.query(User).filter(User.name.in_(names))
    #
    # print(users)
    #
    # if users:
    #     for user in users:
    #         print(f"User ID - {user.id}   |   User name: {user.name}")
    #
    # else:
    #     print("NOT FOUND")

    # ages = [random.randint(65, 75) for _ in range(5)]
    #
    # users = session.query(User).filter(User.age.in_(ages))
    #
    # print(users)
    #
    # if users:
    #     for user in users:
    #         print(f"User ID - {user.id}   |   User name: {user.name}   |   User age: {user.age}")
    #
    # else:
    #     print("NOT FOUND")

    # ages = [random.randint(65, 75) for _ in range(5)]
    #
    # users = session.query(User).filter(User.age.in_(ages))
    #
    # print(users)
    #
    # if users:
    #     for user in users:
    #         print(f"User ID - {user.id}   |   User name: {user.name}   |   User age: {user.age}")
    #
    # else:
    #     print("NOT FOUND")

    # users = session.query(User).filter(and_(User.name.like('J%'), User.age > 70))
    #
    # print(users)
    #
    # if users:
    #     for user in users:
    #         print(f"User ID - {user.id}   |   User name: {user.name}   |   User age: {user.age}")
    #
    # else:
    #     print("NOT FOUND")

    # users = session.query(User).filter(or_(User.name == 'Joseph', User.age == 75))
    #
    # print(users)
    #
    # if users:
    #     for user in users:
    #         print(f"User ID - {user.id}   |   User name: {user.name}   |   User age: {user.age}")
    #
    # else:
    #     print("NOT FOUND")

    # users = session.query(User).filter(not_(User.name.like('J%')))
    #
    # print(users)
    #
    # if users:
    #     for user in users:
    #         print(f"User ID - {user.id}   |   User name: {user.name}   |   User age: {user.age}")
    #
    # else:
    #     print("NOT FOUND")

    # users = session.query(User).filter(User.id.between(1, 10))
    #
    # print(users)
    #
    # if users:
    #     for user in users:
    #         print(f"User ID - {user.id}   |   User name: {user.name}   |   User age: {user.age}")
    #
    # else:
    #     print("NOT FOUND")

    # users = session.query(User).filter(User.id.between(1, 15)).order_by(User.age)
    # users = session.query(User).filter(User.id.between(1, 15)).order_by(desc(User.age))
    #
    # print(users)
    #
    # if users:
    #     for user in users:
    #         print(f"User ID - {user.id}   |   User name: {user.name}   |   User age: {user.age}")
    #
    # else:
    #     print("NOT FOUND")

    # users = session.query(User).filter(
    #     and_(User.age > 55, User.name.like('A%'))
    # ).order_by(desc(User.age))
    #
    # print(users)
    #
    # if users:
    #     for user in users:
    #         print(f"User ID - {user.id}   |   User name: {user.name}   |   User age: {user.age}")
    #
    # else:
    #     print("NOT FOUND")

    users = session.query(User).filter(
        User.age > 55
    ).order_by(User.age, User.name)

    print(users)

    if users:
        for user in users:
            print(f"User ID - {user.id}   |   User name: {user.name}   |   User age: {user.age}")

    else:
        print("NOT FOUND")