from beanie import Document
from pydantic import Field

from src.models.dto import PageSettings
from src.models.responses import Question


class DomainModel(Document):
    """Model for domain and questions in dialog with bot"""

    class Settings:
        name = "domains"

    url: str
    questions: list[Question] = Field(default_factory=list)
    settings: PageSettings = Field(default_factory=PageSettings)
