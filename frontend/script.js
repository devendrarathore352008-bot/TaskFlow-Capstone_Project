const taskForm = document.getElementById("task-form");
const titleInput = document.getElementById("title");
const priorityInput = document.getElementById("priority");
const dueDateInput = document.getElementById("due-date");
const titleError = document.getElementById("title-error");
const taskList = document.getElementById("task-list");

let editingTaskId = null;

function renderTask(task) {

    const taskItem = document.createElement("div");

    taskItem.className = "task-item";

    const title = document.createElement("h3");
    title.textContent = task.title;

    const priority = document.createElement("p");
    priority.textContent = "Priority: " + task.priority;

    const dueDate = document.createElement("p");
    dueDate.textContent = "Due Date: " + (task.due_date || "Not Set");

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";

    const editButton = document.createElement("button");
    editButton.textContent = "Edit";

    editButton.addEventListener("click", function () {
        editingTaskId = task.id;

        titleInput.value = task.title;
        priorityInput.value = task.priority;
        dueDateInput.value = task.due_date || "";
    });

    deleteButton.addEventListener("click", function () {

        fetch(`http://127.0.0.1:8000/tasks/${task.id}`, {
            method: "DELETE"
        })
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {

            console.log(data);

            loadTasks();

        });

});

    taskItem.appendChild(title);
    taskItem.appendChild(priority);
    taskItem.appendChild(dueDate);
    taskItem.appendChild(editButton);
    taskItem.appendChild(deleteButton);

    taskList.appendChild(taskItem);

}

function saveTasksToLocalStorage(tasks) {
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function loadTasksFromLocalStorage() {

    const savedTasks = localStorage.getItem("tasks");

    if (!savedTasks) {
        return;
    }

    const tasks = JSON.parse(savedTasks);

    taskList.textContent = "";

    tasks.forEach(function(task) {
        renderTask(task);
    });

}

function loadTasks() {

    fetch("http://127.0.0.1:8000/tasks/")
        .then(function(response) {
            return response.json();
        })
        .then(function(tasks) {

            saveTasksToLocalStorage(tasks);

            taskList.textContent = "";

            tasks.forEach(function(task) {
                renderTask(task);
        });

});

}

taskForm.addEventListener("submit", function (event) {

    event.preventDefault();

    const title = titleInput.value.trim();

    if (title === "") {

        titleError.textContent = "Task title is required.";

        return;
    }

    titleError.textContent = "";

    const taskData = {
    title: title,
    description: "",
    priority: priorityInput.value,
    due_date: dueDateInput.value,
    project_id: 1
    };

    const url = editingTaskId
        ? `http://127.0.0.1:8000/tasks/${editingTaskId}`
        : "http://127.0.0.1:8000/tasks/";

    const method = editingTaskId ? "PUT" : "POST";

    fetch(url, {
        method: method,
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(taskData)
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {

        loadTasks();

        taskForm.reset();

        titleError.textContent = "";

        editingTaskId = null;

    });

});

loadTasksFromLocalStorage();
loadTasks();