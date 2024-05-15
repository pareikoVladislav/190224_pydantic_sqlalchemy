from alchemy_queries.connector import DBConnector
from alchemy_queries import engine

from alchemy_queries.models import User, Address


with DBConnector(engine=engine) as session:
    # users = session.query(User).join(Address)
    #
    # print(users)
    # print(users.all())
    #
    # for user in users:
    #     print(f"User ID : {user.id}  |  User name: {user.name}")
    #
    #     print("USER ADDRESSES:")
    #     for address in user.addresses:
    #         print(f"ADDRESS ID: {address.id}   |   ADDRESS DESCRIPTION: {address.description}")
    #
    #     print("=" * 90)

    # users = session.query(User).outerjoin(Address)
    #
    # print(users)
    #
    # for user in users:
    #     print(f"User ID : {user.id}  |  User name: {user.name}")
    #
    #     print("USER ADDRESSES:")
    #     for address in user.addresses:
    #         print(f"ADDRESS ID: {address.id}   |   ADDRESS DESCRIPTION: {address.description}")
    #
    #     print("=" * 90)

    users = session.query(User)

    print(users)

    for user in users:
        print(f"User ID : {user.id}  |  User name: {user.name}")

        print("USER ADDRESSES:")
        for address in user.addresses:
            print(f"ADDRESS ID: {address.id}   |   ADDRESS DESCRIPTION: {address.description}")

        print("=" * 90)
