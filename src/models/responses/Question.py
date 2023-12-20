import uuid

from pydantic import BaseModel, Field

from src.models.dto import PageSettings
from src.enums import AnswerInputType, QuestionMessageType, QuestionType


class QuestionMessage(BaseModel):
	type: QuestionMessageType = Field(description="Тип сообщения")
	data: str = Field(description="Данные сообщения")


class AnswerInput(BaseModel):
	type: AnswerInputType = Field(..., description="Тип инпута")
	name: str = Field(..., description="Name инпута")
	placeholder: str = Field(..., description="Placeholder инпута")

	max: int = Field(100, description="Максимальная длина инпута")
	min: int = Field(1, description="Минимальная длина инпута")
	error: str = Field("", description="Сообщение об ошибке")


class Question(BaseModel):
	type: QuestionType = Field(..., description="Тип вопроса")
	messages: list[QuestionMessage] = Field(
		default_factory=list, description="Список сообщений, которые будут отображены в диалоге пользователю"
	)
	data: list[str | AnswerInput] = Field(
		default_factory=list, description="Список вариантов ответов или же список инпутов для ввода данных"
	)


class InitDialogResponse(Question):
	dialog_id: uuid.UUID = Field(default_factory=uuid.uuid4, description="Айди диалога")
	page_settings: PageSettings
