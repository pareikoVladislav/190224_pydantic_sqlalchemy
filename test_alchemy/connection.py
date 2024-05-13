from sqlalchemy.orm import sessionmaker
from test_alchemy import engine
import logging

from models import User, Address

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('sqlalchemy.engine')

logger.setLevel(logging.INFO)


Session = sessionmaker(bind=engine)
session = Session()


# user = User(
#     name="Vlad",
#     surname="Black",
#     age=21,
#     email="vlad.b@yahoo.com"
# )

# new_user = User(
#     name="Dmitry",
#     surname="John",
#     age=25,
#     email="d.john@icloud.com"
# )

# address = Address(
#     user_id=2,
#     description="NEW TEST DESCRIPTION",
#     city="BC",
# )


# session.add(address)

# session.commit()

user = session.query(User).first()

print(user)

print(user.email)

print(user.address.description)

# address = session.query(Address).filter_by(user_id=2).first()
#
# print(address)
#
# print(address.description)
#
# print(address.holder.email)
#
# print(address.holder.addresses[0])

session.close()
