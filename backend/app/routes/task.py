from app.algorithms.searching import linear_search, binary_search
from app.algorithms.sorting import insertion_sort
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskResponse


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    new_task = Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        due_date=task.due_date,
        project_id=task.project_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    sort: str | None = Query(default=None),
    db: Session = Depends(get_db)
):
    tasks = db.query(Task).all()

    if sort == "priority":

        priority_rank = {
            "low": 1,
            "medium": 2,
            "high": 3
        }

        task_records = []

        for task in tasks:
            task_records.append({
                "id": task.id,
                "title": task.title,
                "priority": task.priority,
                "priority_rank": priority_rank[task.priority],
                "due_date": task.due_date,
                "project_id": task.project_id
            })

        insertion_sort(task_records, "priority_rank")

        for task in task_records:
            task.pop("priority_rank")

        return task_records

    return tasks

@router.get("/search/", response_model=TaskResponse)
def search_task(
    title: str,
    algo: str = "linear",
    db: Session = Depends(get_db)
):
    tasks = db.query(Task).all()

    task_records = []

    for task in tasks:
        task_records.append({
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "due_date": task.due_date,
            "project_id": task.project_id,
            "id": task.id
        })

    if algo == "binary":
        insertion_sort(task_records, "title")
        index = binary_search(task_records, title, "title")
    else:
        index = linear_search(task_records, title, "title")

    if index == -1:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task_records[index]

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_data: TaskCreate,
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    task.title = task_data.title
    task.description = task_data.description
    task.priority = task_data.priority
    task.due_date = task_data.due_date
    task.project_id = task_data.project_id

    db.commit()
    db.refresh(task)

    return task

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted successfully"
    }