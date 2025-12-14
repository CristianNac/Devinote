
from sqlmodel import SQLModel, Field

class User(SQLModel, table = True):                  #Al heredar SQLModel viene implicito el uso de SqlAlchemy y pydantic
    id: int = Field(default=None, primary_key = True)
    email: str = Field(index = True, unique = True)
    full_name: str = Field(default="")
    hashed_password: str
    active: bool = Field(default = True)

class UserCreate(SQLModel):                        #Al no poner table True, lo trata como validador de Pydantic
    email: str 
    full_name: str = ""
    password: str 

class UserRead(SQLModel):
    id: int
    email: str
    full_name: str
    model_config = {"from_attributes":True}