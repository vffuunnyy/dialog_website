import datetime
import uuid

from beanie import Document, Link
from pydantic import Field

from src.models.dto import QuestionAnswer


class DialogModel(Document):
    """Model for user dialog with bot"""

    class Settings:
        name = "dialogs"

    dialog_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    answers: list[QuestionAnswer] = Field(default_factory=list)

    ip: str = Field(..., description="User ip")
    user_agent: str = Field(..., description="User agent")
    domain: Link["DomainModel"] = Field(..., description="Domain")
    created_at: datetime.datetime = Field(
        description="Report creation time", default_factory=lambda: datetime.datetime.now(datetime.UTC)
    )
