from bot import utils
from bot.models import Card
import json


class CardService:

    async def get_card(self, id: int):
        response = await utils.card(id)

        card = Card(**response)
        return card.display()

    async def get_recent(self):
        return "hello"
