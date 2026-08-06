from fastapi import FastAPI, Request
import time

from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models import User, Project, Task

from app.routes.project import router as project_router
from app.routes.user import router as user_router
from app.routes.task import router as task_router
from app.routes.statistics import router as statistics_router
from app.routes.quick_add import router as quick_add_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=[
        "GET",
        "POST",
        "PUT",
        "DELETE"
    ],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000

    print(
        f"{request.method} {request.url.path} "
        f"- {process_time:.2f} ms"
    )

    return response

app.include_router(project_router)
app.include_router(user_router)
app.include_router(task_router)
app.include_router(quick_add_router)
app.include_router(statistics_router)

@app.get("/")
def home():
    return {"message": "TaskFlow API is running"}