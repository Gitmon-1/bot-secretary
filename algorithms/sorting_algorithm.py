import asyncio
import json
import os
from algorithms.category import catalog, keywords
from bot.convertor import save_to_json2

categorized = {cat: [] for cat in keywords.keys()}
default_category = {cat: [] for cat in keywords.keys()} #TODO


async def sorting(data: dict, catalog):
    """"Алгоритм сортировки сообщений из не сортированого JSON file в сортированный"""

    for msg in data.get("messages", []):
        msg_lower = msg.lower()
        found = False

        for k, v in keywords.items():
            if any(word in msg_lower for word in v or k): 
                    categorized[k].append(msg) 
                    found = True
                    
            if not found:
                return default_category[k].append(msg) #TODO
    return await save_to_json2(categorized)
    

