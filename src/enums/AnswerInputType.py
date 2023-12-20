from enum import StrEnum


class AnswerInputType(StrEnum):
	"""HTML input types"""

	PHONE = "tel"
	TEXT = "text"
	EMAIL = "email"
	NUMBER = "number"
	PASSWORD = "password"  # noqa: S105
