from pydantic import BaseModel


class UserAddress(BaseModel):
    city: str
    street: str
    house_number: int


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    # is_active: bool = True
    address: UserAddress


# user = User(
#     id=1,
#     name="Vlad",
#     surname="Black",
#     age=24
# )

# wrong_user = User(
#     id="1.",
#     name="Vlad",
#     age=[2, 4, 6],
#     is_active=False
# )

us_address = UserAddress(
    city="Batumi",
    street="Pushkina St.",
    house_number=123
)


user_info = User(
    id=1,
    name="David",
    surname="Agmashenebeli",
    age=37,
    address=us_address
)

print(us_address)
print("=" * 100)
print(user_info)
print(f"User's name {user_info.name}. User's city: {user_info.address.city}")


# user_info = {
#     "id": 1,
#     "name": "Vlad",
#     "surname": "Black",
#     "age": 37,
#     "address": {
#         "city": "Batumi",
#         "street": "Street 1",
#         "house_number": 123
#     }
# }