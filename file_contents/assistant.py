content = """
import json
from fastapi import APIRouter, Form, status, BackgroundTasks

from src.services.twilio.twilio import send_message
from src.services.llm.agent import ask_assistant

router = APIRouter(tags=["assistant"])


@router.post("/assistant-message", status_code=status.HTTP_200_OK)
async def ask_clara(
    Body: str = Form(default=None),
    From: str = Form(),
    ProfileName: str = Form(),
):
    "Asks Clara a question regarding Simplicar"
    resp = await ask_assistant(
        json.dumps(
            {
                "human_message": Body.lower() if Body else "",
                "wa_id": From,
                "wa_name": ProfileName,
                "timestamp": "1",
            }
        )
    )
    return send_message(resp, From)
"""