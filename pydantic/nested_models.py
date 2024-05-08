from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr

    def greeting(self):
        return f"Hello, my name is {self.name}"

    def __str__(self):
        return f"User '{self.name}' have an email '{self.email}'"


class AdminUser(User):
    is_superuser: bool
    access_level: int

    def __str__(self):
        return f"Admin '{self.name}' have an access level '{self.access_level}'"


user = User(name="Vlad", email="test.email@gmail.com")

print(user)

admin = AdminUser(name="Bob", email="test.bob@yahoo.com", is_superuser=True, access_level=10)

print(admin)

print(f"Ordinary user: {user.name}. Email - {user.email}")


print(f"Admin user: {admin.name}. Email - {admin.email}. Access level = {admin.access_level}")

print(user.greeting())

print(admin.greeting())
