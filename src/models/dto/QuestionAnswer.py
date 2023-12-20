from pydantic import BaseModel

from src.models.responses import Question


class QuestionAnswer(BaseModel):
	question: Question
	answer: str | dict
