from pydantic import BaseModel


class PageSettings(BaseModel):
	title: str = ""
	bot_icon: str = ""
	bot_name: str = ""
