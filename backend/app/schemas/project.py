from pydantic import BaseModel


class ProjectCreate(BaseModel):
    name: str
    owner_id: int


class ProjectResponse(ProjectCreate):
    id: int

    class Config:
        from_attributes = True