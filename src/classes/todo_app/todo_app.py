"""
Application module
"""
# import os
from datetime import datetime
from pathlib import Path

from src.classes.todo_app.models.task import Task
# from src.classes.todo_app.models.category import Category
# from src.classes.todo_app.models.status import Status
from src.classes.todo_app.repositories.task_repository import TaskRepository
from src.classes.todo_app.repositories.category_repository import CategoryRepository
from src.classes.todo_app.repositories.status_repository import StatusRepository


class TodoApp:
    """
    Основной класс приложения для управления задачами.
    Предоставляет доступ к репозиториям и методы с бизнес-логикой.
    """
    def __init__(self, data_dir: str):
        """
        Инициализация приложения.
        
        Args:
            data_dir: Путь к директории с JSON файлами данных
        """
        # Создайте репозитории и сохраните их как атрибуты:
        self.data_dir = data_dir
        self.task_repo = TaskRepository(data_dir)
        self.category_repo = CategoryRepository(data_dir)
        self.status_repo = StatusRepository(data_dir)

    def add_task(self, title: str, category_id: int, status_id: int, **kwargs) -> Task:
        """
        Добавить новую задачу с проверкой существования категории и статуса.
        
        Args:
            title: Заголовок задачи
            category_id: ID категории
            status_id: ID статуса
            **kwargs: Дополнительные параметры (description, deadline, repeat_every)
            
        Returns:
            Созданная задача
            
        Raises:
            ValueError: Если категория или статус не существуют
        """
        # 1. Проверьте существование категории и статуса
        if not self.category_repo.get(category_id):
            raise ValueError(f"The category {category_id} is not exist")

        if not self.status_repo.is_valid_status(status_id):
            raise ValueError(f"The status {status_id} is not exist")

        # 2. Получите следующий ID для задачи
        next_id = len(self.task_repo.get_all()) + 1

        # 3. Создайте задачу и добавьте её через репозиторий
        task = Task(id=next_id, title=title, category_id=category_id,
                    status_id=status_id, **kwargs)
        return self.task_repo.add(task)

    def mark_task_done(self, task_id: int) -> bool:
        """
        Отметить задачу как выполненную.
        
        Args:
            task_id: ID задачи

        Returns:
            True, если задача обновлена, False если не найдена
        """
        self.task_repo.update(task_id, is_done=True)

    def get_overdue_tasks(self) -> list[Task]:
        """
        Получить просроченные задачи.
        
        Returns:
            Список задач с истекшим дедлайном
        """
        # Получите все задачи и отфильтруйте те, у которых:
        # - есть дедлайн
        # - дедлайн истек (меньше текущего времени)
        # - задача не выполнена
        overdue_tasks = []
        for task in self.task_repo.get_all():
            if task.deadline and datetime.now() > task.deadline and not task.is_done:
                overdue_tasks.append(task)
        return overdue_tasks


def load_sample_data(app: TodoApp) -> None:
    """
    Загрузить примерные данные в приложение.
    
    Args:
        app: Экземпляр TodoApp
    """
    dir_data = Path(app.data_dir)

    app.task_repo.__init__(dir_data / "tasks.json")
    app.category_repo.__init__(dir_data / "categories.json")
    app.status_repo.__init__(dir_data / "statuses.json")


def print_task(task: Task) -> None:
    """
    Вывести информацию о задаче.
    
    Args:
        task: Задача для вывода
    """
    info = f"""\
    ID: {task.id}
    Заголовок: {task.title}
    Описание: {task.description}
    Дата создания: {task.created_at}
    ID категории: {task.category_id}
    ID статуса: {task.status_id}
    Выполнена: {task.is_done}
    Срок выполнения: {task.deadline}
    Периодичность: every {task.repeat_every}\
    """
    print("========= Инфо о задаче =========")
    print(info)
    print("=================================\n")


def print_tasks(tasks: list[Task]) -> None:
    """
    Вывести список задач.
    
    Args:
        tasks: Список задач для вывода
    """
    for task in tasks:
        print_task(task)


if __name__ == "__main__":
    # Пример использования
    app = TodoApp("src/classes/todo_app/data")

    # Загружаем примерные данные
    load_sample_data(app)

    print("=== Все задачи ===")
    # Теперь работаем с репозиторием напрямую
    all_tasks = app.task_repo.get_all()
    print_tasks(all_tasks)

    print("\n=== Задачи по категории 'Учеба' ===")
    study_tasks = app.task_repo.get_by_category(3)
    print_tasks(study_tasks)

    print("\n=== Просроченные задачи ===")
    overdue_tasks = app.get_overdue_tasks()
    print_tasks(overdue_tasks)

    # Добавляем новую задачу через высокоуровневый API
    print("\n=== Добавляем новую задачу ===")
    new_task = app.add_task(
        title="Новая задача",
        category_id=1,
        status_id=1,
        description="Это новая задача для демонстрации"
    )
    print_task(new_task)
