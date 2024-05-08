from pydantic import BaseModel, Field, HttpUrl
from typing import List


class Owner(BaseModel):
    name: str = Field(..., min_length=3, max_length=15)
    age: int = Field(..., ge=18, le=99)
    homepage: HttpUrl


class Product(BaseModel):
    name: str
    description: str = Field(None, description="OUR FIRST DESCRIPTION FOR FIELD")
    price: float = Field(gt=0, description="WE NEED TO PROVIDE A PRICE MORE THAN 0")
    available: bool = Field(True, alias="in_stock")
    tags: List[str]


product = Product(
    name="Table",
    description="Awesome table!!!",
    price=12,
    tags=["table"]
)

print(product)


owner = Owner(
    name="Yan",
    age=20,
    homepage="https://www.qwerty.com"
)

print(owner)
