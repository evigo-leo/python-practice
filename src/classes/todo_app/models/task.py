from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class Task(BaseModel):
    model_config = ConfigDict()

    id: int
    title: str = Field(..., min_length=3, max_length=100)
    description: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)
    category_id: int
    status_id: int

    # Optional fields for different task behaviors
    is_done: bool | None = None  # For simple tasks
    deadline: datetime | None = None  # For urgent tasks
    repeat_every: str | None = None  # For recurring tasks ("day", "week", "month")

    def model_post_init(self, __context) -> None:
        """Set default values for optional fields"""
        if self.is_done is None:
            self.is_done = False
