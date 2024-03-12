import requests
import json
import config


async def card(id: int):
    response = requests.get(f"{config.WB_API}{id}")
    response = json.loads(response.text)['data']['products'][0]
    return response
