from datetime import date
from pydantic import BaseModel, ConfigDict

class UserSchema(BaseModel):
    id: int
    name: str = "John Doe"
    birthday_date: date

    config = ConfigDict(from_attributes=True)

user1 = UserSchema.from_object(orm_instance)