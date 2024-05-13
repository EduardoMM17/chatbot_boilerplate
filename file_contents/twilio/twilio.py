content = """
import os

from src.services.twilio.client import client
from src.services.twilio.utils import split_text_recursively


def send_message(body_text: str, to: str):
    l = split_text_recursively(body_text)
    for i in l:
        client.messages.create(
            from_=os.environ["TWILIO_WA_NUMBER"],
            body=i,
            to=to,
        )

"""