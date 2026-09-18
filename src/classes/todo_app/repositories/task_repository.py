"""
Task repo module
"""
from src.classes.todo_app.models.task import Task
from src.classes.todo_app.repositories.base_repository import BaseRepository

class TaskRepository(BaseRepository[Task]):
    def __init__(self, file_path: str):
         super().__init__(file_path=file_path, model=Task)

    def get_by_category(self, category_id: int) -> list[Task]:
        """Get all tasks belonging to a specific category."""
        tasks_by_category = []
        for task in self.get_all():
            if task.category_id == category_id:
                tasks_by_category.append(task)
        return tasks_by_category
        
    def get_by_status(self, status_id: int) -> list[Task]:
        """Get all tasks with a specific status."""
        tasks_by_status = []
        for task in self.get_all():
            if task.status_id == status_id:
                tasks_by_status.append(task)
        return tasks_by_status
