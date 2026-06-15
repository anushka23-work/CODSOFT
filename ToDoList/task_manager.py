import json

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({
        "task": task,
        "status": "Pending"
    })
    save_tasks(tasks)

def view_tasks():
    return load_tasks()

def mark_completed(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["status"] = "Completed"
        save_tasks(tasks)

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)