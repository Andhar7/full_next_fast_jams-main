
# Modern approach:
from pydantic import BaseModel

class ToDoBase(BaseModel):
    name: str
    completed: bool = False

    model_config = {
        "from_attributes": True  # This is the new way in Pydantic v2
    }

class ToDoRequest(ToDoBase):
    pass

class ToDoResponse(ToDoBase):
    id: int




# from pydantic import BaseModel

# class ToDoRequest(BaseModel):
#     name: str
#     completed: bool

# class ToDoResponse(BaseModel):
#     name: str
#     completed: bool
#     id: int

#     class Config:
#         orm_mode = True