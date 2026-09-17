"""
Base repository module
"""
import json
import os
from datetime import datetime
from json import JSONEncoder

from pydantic import BaseModel


class DateTimeEncoder(JSONEncoder):
    """The encoder class for transformation datetime"""
    def default(self, obj):
        """Transform datetime"""
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


class BaseRepository[T: BaseModel]:
    """The base class for repo"""
    def __init__(self, file_path: str, model: type[T]):
        self._file_path: str = os.path.join(file_path)
        self._model: T = model
        self._data: dict[int, T] = {}

        # Загружаем существующие данные, если файл уже есть
        if os.path.exists(self._file_path):
            self._load()

    def _load(self) -> None:
        """Load data from file"""
        try:
            with open(self._file_path, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
                # Переводим строковые ключи JSON в int и валидируем через Pydantic-модель
                self._data = {
                    int(k): self._model.model_validate(v)
                    for k, v in raw_data.items()
                }
        except (json.JSONDecodeError, FileNotFoundError):
            self._data = {}

    def _save(self) -> None:
        """Save data to file"""
        # Сериализуем Pydantic-модели в dict/JSON-совместимый формат
        # Используем .model_dump(), а для дат — кастомный DateTimeEncoder
        serialized_data = {
            str(k): v.model_dump()
            for k, v in self._data.items()
        }

        # Создаем директорию, если она еще не создана
        dir_name = os.path.dirname(self._file_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        with open(self._file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_data, f, cls=DateTimeEncoder)

    def add(self, item: T) -> T:
        """Add an element"""
        if item.id in self._data:
            raise ValueError(f"Item with id {item.id} already exists")

        self._data[item.id] = item
        self._save()
        return item

    def get(self, id_: int) -> T | None:
        """Get an element by id"""
        return self._data.get(id_)

    def get_all(self) -> list[T]:
        """Get all elements"""
        return list(self._data.values())

    def update(self, id_: int, **kwargs) -> bool:
        """Update an element"""
        if id_ not in self._data:
            return False

        current_item = self._data[id_]
        # Извлекаем текущие поля, обновляем переданными kwargs и создаем новый валидный объект
        updated_data = current_item.model_dump()
        updated_data.update(kwargs)

        self._data[id_] = self._model.model_validate(updated_data)
        self._save()
        return True

    def delete(self, id_: int) -> bool:
        """Delete an element"""
        if id_ not in self._data:
            return False

        del self._data[id_]
        self._save()
        return True
