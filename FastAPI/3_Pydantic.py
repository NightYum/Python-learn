from fastapi import FastAPI

from pydantic import BaseModel, Field, EmailStr, ConfigDict

app = FastAPI()

data = {
     "email": "abc@gmail.com",
     "bio": None,
     "age": 18,
 }

data_wo_age = {
     "email": "abc@gmail.com",
     "bio": None,
    # "gender": "male",
    # "language": "en",
 }

class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=22)

    model_config = ConfigDict(extra="forbid")

class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=130)

users = []

@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)
    return {"success": True, "message": "Пользователь добавлен"}

@app.get("/users")
def get_users() -> list[UserSchema]:
    return users


# user1 = UserAgeSchema(**data)
# user2 = UserSchema(**data_wo_age)
# print(repr(user1))
# print(repr(user2))
