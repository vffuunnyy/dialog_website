import asyncio

from beanie import init_beanie
from config import MONGO_DB, MONGO_URI
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient

from src.enums import AnswerInputType, QuestionMessageType, QuestionType
from src.models.db import DialogModel, DomainModel
from src.models.dto.PageSettings import PageSettings
from src.models.responses import AnswerInput, Question, QuestionMessage


async def main() -> None:
    logger.info("Connecting to MongoDB")
    logger.info(MONGO_URI)

    await init_beanie(
        database=AsyncIOMotorClient(MONGO_URI)[MONGO_DB],
        document_models=[DialogModel, DomainModel],
    )

    await DomainModel(
        url="sosiska.work",
        questions=[
            Question(
                type=QuestionType.INPUT,
                messages=[
                    QuestionMessage(
                        type=QuestionMessageType.TEXT,
                        data="Привет",
                    ),
                    QuestionMessage(
                        type=QuestionMessageType.TEXT,
                        data="Введите ваше имя",
                    ),
                ],
                data=[
                    AnswerInput(type=AnswerInputType.TEXT, placeholder="Ваше Имя", name="first_name", error="Обязательное поле"),
                    AnswerInput(
                        type=AnswerInputType.TEXT, placeholder="Ваша Фамилия", name="last_name", error="Обязательное поле"
                    ),
                ],
            ),
            Question(
                type=QuestionType.OPTION,
                messages=[
                    QuestionMessage(
                        type=QuestionMessageType.TEXT,
                        data="Теперь меня интересует другое.<br>Во-первых посмотри на котика",
                    ),
                    QuestionMessage(
                        type=QuestionMessageType.IMAGE,
                        data="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPt4C0lnPBd_OhaGmL1d6Bs4_mSUz4VvLaJZZ6QBBRJw&s",
                    ),
                    QuestionMessage(
                        type="text",
                        data="А теперь скажи свой гендер",
                    ),
                ],
                data=["Мужской", "Женский", "Posudomoyka", "Attack Helicopter"],
            ),
            Question(
                type=QuestionType.INPUT,
                messages=[
                    QuestionMessage(
                        type=QuestionMessageType.TEXT,
                        data="Теперь дай сюда номер телефона или палучиш папопе",
                    ),
                ],
                data=[
                    AnswerInput(
                        type=AnswerInputType.PHONE,
                        placeholder="",
                        name="phone_number",
                        error="Введите номер телефона",
                        min=9,
                        max=20,
                    ),
                ],
            ),
            Question(
                type=QuestionType.END, messages=[QuestionMessage(type=QuestionMessageType.TEXT, data="Спс. Изи скам.")]
            ),
        ],
        settings=PageSettings(
            title="Чат с сосисками",
            bot_name="Сосиска",
            bot_icon="https://sosiska.work/assets/favicon-W-QH7cso.svg",
        ),
    ).create()


if __name__ == "__main__":
    asyncio.run(main())
