from fastapi import APIRouter, Depends
from sqlalchemy import func, case
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.project import Project
from app.models.task import Task
from app.schemas.statistics import ProjectStatistics


router = APIRouter(
    prefix="/statistics",
    tags=["Statistics"]
)


@router.get("/projects", response_model=list[ProjectStatistics])
def project_statistics(
    db: Session = Depends(get_db)
):
    results = (
        db.query(
            Project.id.label("project_id"),
            Project.name.label("project_name"),
            func.count(Task.id).label("total_tasks"),
            func.sum(
                case(
                    (Task.status == "pending", 1),
                    else_=0
                )
            ).label("pending_tasks"),
        )
        .outerjoin(Task, Project.id == Task.project_id)
        .group_by(Project.id, Project.name)
        .all()
    )

    return results