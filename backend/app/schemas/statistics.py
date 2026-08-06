from pydantic import BaseModel


class ProjectStatistics(BaseModel):
    project_id: int
    project_name: str
    total_tasks: int
    pending_tasks: int