# TaskFlow

## About

TaskFlow is a Full-Stack AI-Assisted Task Management Platform developed as a Capstone Project during my Software Development Engineering program at Masai School.

The project focuses on building a task management system with a FastAPI backend, database integration, frontend interface, algorithm-based features, and AI-assisted task creation.

## Features

- User Management
- Project Management
- Task CRUD
- Task Statistics
- Task Sorting using Insertion Sort
- Task Searching using Linear Search and Binary Search
- AI Quick Add (Rule-based Mock Parser)
- Responsive Frontend
- LocalStorage Cache

---

## Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite

### Frontend
- HTML
- CSS
- JavaScript

---

## Setup

Create virtual environment

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Install packages

```bash
pip install -r requirements.txt
```

Run backend

```bash
uvicorn app.main:app --reload
```

Open frontend using Live Server.

---

## API Endpoints

### Users

- POST /users/
- GET /users/

### Projects

- POST /projects/
- GET /projects/

### Tasks

- POST /tasks/
- GET /tasks/
- GET /tasks/{id}
- PUT /tasks/{id}
- DELETE /tasks/{id}

### Statistics

- GET /statistics/

### Algorithms

- GET /tasks?sort=priority

- GET /tasks/search?title=Task Name&algo=linear

- GET /tasks/search?title=Task Name&algo=binary

### AI

- POST /tasks/quick-add

---

## Algorithm Complexity

| Algorithm | Best | Worst |
|-----------|------|-------|
| Insertion Sort | O(n) | O(n²) |
| Linear Search | O(1) | O(n) |
| Binary Search | O(1) | O(log n) |

---

## Benchmark

| Tasks | Insertion Sort | Linear Search | Binary Search |
|------:|---------------:|--------------:|--------------:|
| 10 | 9 | 10 | 4 |
| 500 | 499 | 500 | 9 |
| 3000 | 2999 | 3000 | 12 |

The benchmark shows that Binary Search performs significantly fewer comparisons than Linear Search as the dataset grows. Although sorting has an initial cost, it becomes worthwhile when the task list is searched repeatedly.

---

## AI Quick Add

The project uses a deterministic rule-based mock parser.

It extracts:

- Title
- Priority
- Due Date

Priority values:

- low
- medium
- high

The parser does not require any API key or internet connection.

---

## Example Inputs

Input

```
Finish report tomorrow urgent
```

Output

```json
{
"title":"Finish report",
"priority":"high",
"due_date":"tomorrow"
}
```

Input

```
Complete assignment next friday
```

Output

```json
{
"title":"Complete assignment",
"priority":"medium",
"due_date":"next friday"
}
```

Input

```
Low priority clean room whenever
```

Output

```json
{
"title":"clean room",
"priority":"low",
"due_date":null
}
```

Input

```
Submit project ASAP today
```

Output

```json
{
"title":"Submit project",
"priority":"high",
"due_date":"today"
}
```

Input

```
Prepare presentation monday
```

Output

```json
{
"title":"Prepare presentation",
"priority":"medium",
"due_date":"monday"
}
```
## Creator
Devendra Rathore