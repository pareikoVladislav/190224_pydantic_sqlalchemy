from pydantic import BaseModel, field_validator, Field, EmailStr


class User(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=25,
        alias="username"
    )
    age: int = Field(
        ...,
        gt=0,
        le=122
    )
    email: EmailStr

    @field_validator('email')
    def check_email(cls, value: EmailStr):
        allow_domains = ['gmail.com', 'yahoo.com']

        # "test.email@gmail.com" -> ["test.email", "gmail.com"] -> "gmail.com"
        email_domain = value.split("@")[-1]

        if email_domain not in allow_domains:
            raise ValueError(f"Email must be from one of these domains: {', '.join(allow_domains)}")

        return value  # -> validated data

    class Config:
        str_strip_whitespace = True
        validate_assignment = True
        # str_min_length = 3
        # json_encoders = {
        #     datetime: lambda value: value.strftime('%Y-%m-%d'),
        # }


try:
    user_with_valid_email = User(
        username="Vlad",
        age=27,
        email="vlad.black@gmail.com"
    )
    print(f"User {user_with_valid_email.name}. Email - {user_with_valid_email.email}")

    # user_with_valid_email.age = "qwerty"
    user_with_valid_email.age = 28

    print(f"User's age = {user_with_valid_email.age}")

    user_with_bad_email = User(
        username="Vlad",
        age=27,
        email="vlad.black@yahoo.com"
    )
except ValueError as err:
    print(err)

