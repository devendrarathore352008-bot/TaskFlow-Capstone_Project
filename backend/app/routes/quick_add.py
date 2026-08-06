from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.task import Task
from app.models.project import Project
from app.schemas.quick_add import QuickAddRequest
from app.schemas.task import TaskResponse
from app.ai.mock_parser import parse_task

router = APIRouter(
    prefix="/tasks",
    tags=["Quick Add"]
)


@router.post("/quick-add", response_model=TaskResponse, status_code=201)
def quick_add(data: QuickAddRequest, db: Session = Depends(get_db)):

    project = db.query(Project).filter(Project.id == data.project_id).first()

    if not project:
        raise HTTPException(status_code=422, detail="Project not found")

    parsed = parse_task(data.description)

    task = Task(
        title=parsed["title"],
        description=data.description,
        priority=parsed["priority"],
        due_date=parsed["due_date_hint"],
        project_id=data.project_id
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task