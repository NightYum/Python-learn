from pydantic import BaseModel, field_validator, computed_field
from datetime import date

class UserSchema(BaseModel):
    first_name: str
    last_name: str
    age: int
    date_registration: date


    @field_validator('first_name')
    @classmethod
    def check_first_name(cls, value):
        if 3 < len(value) > 12:
            raise ValueError('Not a valid first name')
        return value

    @field_validator('last_name')
    @classmethod
    def check_last_name(cls, value):
        if 3 < len(value) > 12:
            raise ValueError('Not a valid last name')
        return value

    @field_validator('age', mode="after")
    @classmethod
    def check_age(cls, value):
        if value < 18:
            raise ValueError('18+')
        return value

    @computed_field
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'


data_user_1 = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 18
}

data_user_2 = {
    "first_name": "Mikhail",
    "last_name": "Erastov",
    "age": "18" # Pydantic автоматически преобразует данные
}

user_john = UserSchema(**data_user_1)
user_mikhail = UserSchema(**data_user_2)

to_dict = user_mikhail.model_dump()
to_json = user_mikhail.model_dump_json()

print(to_dict,type(to_dict))
print(to_json,type(to_json))

try:
    user = UserSchema(id=1, first_name="John", last_name="Doe", age=18)