from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    completed: bool = False


class TodoUpdate(BaseModel):
    title: str
    completed: bool


class Todo(BaseModel):
    id: int
    title: str
    completed: bool

    class Config:
        from_attributes = True