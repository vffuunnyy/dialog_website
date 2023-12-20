import uuid

from pydantic import BaseModel, Field


class Answer(BaseModel):
	question_id: int = Field(..., description="Айди вопроса")
	dialog_id: uuid.UUID = Field(..., description="Айди диалога")
	answers: str | dict = Field(..., description=r"Ответ\ы на вопрос")
