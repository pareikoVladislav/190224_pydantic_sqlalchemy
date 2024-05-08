from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    surname: str
    email: EmailStr

    def __str__(self):
        return f"User {self.name}, Email: {self.email}"


class AdminUser(User):
    access_level: int

    def __str__(self):
        return f"Admin {self.name}, Access Level: {self.access_level}"

    def promote_user(self, user: User):
        print(f"Promoting User '{user.name}' to a higher role")

        return AdminUser(
            name=user.name,
            surname=user.surname,
            email=user.email,
            access_level=self.access_level + 1
        )


ordinary_user = User(
    name="Vlad",
    surname="Black",
    email="vlad.black@yahoo.com",
)

print(ordinary_user)


print("=" * 100)

admin_user = AdminUser(
    name="John",
    surname="Green",
    email="g.green@gmail.com",
    access_level=5
)

print(admin_user)
print("=" * 100)


new_admin = admin_user.promote_user(user=ordinary_user)

print(new_admin)
