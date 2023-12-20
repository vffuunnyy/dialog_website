from typing import Annotated

from fastapi import APIRouter, Depends
from loguru import logger

from src.depends import get_nginx_headers
from src.models.db import DialogModel, DomainModel
from src.models.dto import NginxHeadersModel, PageSettings, QuestionAnswer
from src.models.requests import Answer
from src.models.responses import InitDialogResponse, Question, QuestionMessage


router = APIRouter()


@router.post("/init_dialog")
async def init_dialog(nginx_headers: Annotated[NginxHeadersModel, Depends(get_nginx_headers)]) -> InitDialogResponse:
    logger.info(nginx_headers)

    domain: DomainModel = await DomainModel.find_one({DomainModel.url: nginx_headers.host})

    if not domain:
        return InitDialogResponse(
            type="end",
            messages=[
                QuestionMessage(
                    type="text",
                    data="Error",
                ),
            ],
            page_settings=PageSettings(
                title="Error",
                bot_icon="",
                bot_name="Error",
            ),
        )

    dialog = DialogModel(
        ip=nginx_headers.x_real_ip,
        user_agent=nginx_headers.user_agent,
        domain=domain.to_ref(),
    )
    await dialog.create()

    return InitDialogResponse(
        **domain.questions[0].model_dump(),
        dialog_id=dialog.dialog_id,
        page_settings=domain.settings,
    )


@router.post("/answer")
async def answer_and_get_next_question(answer: Answer) -> Question | str:
    dialog = await DialogModel.find_one({DialogModel.dialog_id: answer.dialog_id})

    if not dialog:
        return Question(
            type="end",
            messages=[
                QuestionMessage(
                    type="text",
                    data="Error",
                ),
            ],
        )

    domain = await dialog.domain.fetch()
    dialog.answers.append(
        QuestionAnswer(
            question=domain.questions[answer.question_id],
            answer=answer.answers
        )
    )
    await dialog.save()

    question = domain.questions[answer.question_id + 1] if answer.question_id + 1 < len(domain.questions) else None

    if not question:
        return Question(
            type="end",
            messages=[
                QuestionMessage(
                    type="image",
                    data="./assets/succes.png",
                ),
            ],
        )

    return question

