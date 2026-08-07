# TaskFlow
A Full-Stack AI-Assisted Task Management Platform built using FastAPI, SQLAlchemy, SQLite, HTML, CSS, and JavaScript.

## About

TaskFlow is a Full-Stack AI-Assisted Task Management Platform developed as the Capstone Project for the Software Development Engineering Program at Masai School.

The application enables users to create projects, manage tasks, monitor task statistics, search and sort tasks using custom algorithms, and quickly create tasks from natural language using a deterministic AI mock parser.

---

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

## Repository Structure

```text
TaskFlow/
├── backend/
│   ├── app/
│   ├── requirements.txt
│   └── taskflow.db
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── benchmark.py
├── check_algorithms.py
├── README.md
└── requirements.txt
```
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
---

## Running the Application

### Backend

```bash
cd backend
uvicorn app.main:app --reload
```

Backend Runs At

```text
http://127.0.0.1:8000
```


### Frontend

Open the `frontend/index.html` file using the **Live Server** extension in VS Code.

The frontend communicates with the FastAPI backend running at:

```
http://127.0.0.1:8000
```

Frontend Runs At:

```text
http://127.0.0.1:5500
```
---

## Database

The project uses **SQLite** as the database and **SQLAlchemy ORM** for database operations.

### Tables

- Users
- Projects
- Tasks

### Relationships

- One User can have multiple Projects.
- One Project can have multiple Tasks.

## API Endpoints

### Users

- POST /users/ → Create a new user
- GET /users/ → Retrieve all users

### Projects

- POST /projects/ → Create a new project
- GET /projects/ → Retrieve all projects

### Tasks

- POST /tasks/ → Create a task
- GET /tasks/ → Retrieve all tasks
- GET /tasks/{id} → Retrieve a task by ID
- PUT /tasks/{id} → Update a task
- DELETE /tasks/{id} → Delete a task

### Statistics

- GET /statistics/ → Retrieve project task statistics

### Algorithms

- GET /tasks?sort=priority → Sort tasks using Insertion Sort
- GET /tasks/search?title=Task Name&algo=linear → Search using Linear Search
- GET /tasks/search?title=Task Name&algo=binary → Search using Binary Search

### AI

- POST /tasks/quick-add → Create a task from a natural language description

---

## API Examples

### Create User

**Request**

```json
{
  "name": "Devendra",
  "email": "devendra@example.com"
}
```

**Response**

```json
{
  "id": 1,
  "name": "Devendra",
  "email": "devendra@example.com"
}
```

### Create Task

**Request**

```json
{
  "title": "Complete README",
  "priority": "high",
  "project_id": 1
}
```

**Response**

```json
{
  "id": 1,
  "title": "Complete README",
  "priority": "high",
  "project_id": 1
}
```

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

## AI Prompting Technique

The AI Quick Add feature follows a **Zero-Shot Prompting** approach.

Instead of using an external Large Language Model (LLM), this project uses a deterministic rule-based mock parser. The parser extracts the task title, priority, and due date from natural language while producing consistent results without requiring an API key or internet connection.

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

---

## License

This project was developed for educational purposes as part of the Software Development Engineering Program at Masai School.

---

## Author

**Devendra Rathore**

Software Development Engineering Student

Masai School