import asyncio
import json
from pprint import pprint
from typing import Dict, Any

import aiohttp
from settings import ExchangeConfig

headers = {
    "authority": "www.kith.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",
    "sec-fetch-dest": "document",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "accept-language": "en-US,en;q=0.9",
}


async def find_kzt_to_rub(data: Dict[str, Any]) -> str:
    if data.get("result", None):
        for rate in data["result"]:
            if rate["from"] == ExchangeConfig.RUB and rate["to"] == ExchangeConfig.KZT:
                return rate["rate"]
    raise ValueError("Not found value")


async def get_kzt_curs():
    async with aiohttp.ClientSession() as session:
        async with session.get(ExchangeConfig.URL, allow_redirects=True) as response:
            return await find_kzt_to_rub(json.loads(await response.text()))


if __name__ == "__main__":
    print(asyncio.run(get_kzt_curs()))
