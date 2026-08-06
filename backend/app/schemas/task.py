from pydantic import BaseModel, Field, field_validator
from typing import Literal


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    priority: Literal["low", "medium", "high"]
    due_date: str | None = None
    project_id: int


    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if not value.strip():
            raise ValueError("Title cannot be blank")

        return value.strip()


class TaskResponse(TaskCreate):
    id: int

    class Config:
        from_attributes = True