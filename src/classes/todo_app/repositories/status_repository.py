"""
Status repo module
"""
import os
from src.classes.todo_app.models.status import Status
from src.classes.todo_app.repositories.base_repository import BaseRepository


class StatusRepository(BaseRepository[Status]):
    """Class for status repo"""
    def __init__(self, file_path: str):
        super().__init__(file_path=file_path, model=Status)
        if not self._data:
            self._init_default_statuses()

    def _init_default_statuses(self) -> None:
        """Initialize default statuses"""
        default_statuses = [
            Status(id=1, name="В ожидании"),
            Status(id=2, name="В работе"),
            Status(id=3, name="Завершено")
        ]

        for status in default_statuses:
            self._data[status.id] = status
        
        #self._save()

    def is_valid_status(self, status_id: int) -> bool:
        """Check a status valid"""
        return status_id in self._data
