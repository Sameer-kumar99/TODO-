# app/services.py

class TodoService:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, title):
        if not title or title.strip() == "":
            raise ValueError("Title is required")
        task = {"id": self.next_id, "title": title, "done": False}
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        return self.tasks

    def mark_done(self, task_id):
        for t in self.tasks:
            if t["id"] == task_id:
                t["done"] = True
                return t
        raise KeyError("Task not found")

    def update_task(self, task_id, new_title):
        if not new_title or new_title.strip() == "":
            raise ValueError("Title is required")
        for t in self.tasks:
            if t["id"] == task_id:
                t["title"] = new_title
                return t
        raise KeyError("Task not found")

    def delete_task(self, task_id):
        for i, t in enumerate(self.tasks):
            if t["id"] == task_id:
                del self.tasks[i]
                return
        raise KeyError("Task not found")

