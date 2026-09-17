"""Category Repository module"""
from src.classes.todo_app.models.category import Category
from src.classes.todo_app.repositories.base_repository import BaseRepository


class CategoryRepository(BaseRepository[Category]):
    """The category class repo"""
    def __init__(self, file_path: str):
        super().__init__(file_path=file_path, model=Category)

    def get_by_name(self, name: str) -> Category | None:
        """Get category by a name"""
        target_name = name.lower()
        for category in self.get_all():
            if category.name.lower() == target_name:
                return category
        return None
