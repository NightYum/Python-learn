from pydantic import BaseModel, field_validator, computed_field

class UserSchema(BaseModel):
    first_name: str
    last_name: str
    age: int

    @field_validator('age', mode="after")
    @classmethod
    def check_age(cls, value):
        if value < 18:
            raise ValueError('age must be at least 18')
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