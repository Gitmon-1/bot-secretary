import asyncio
import json
import os
from algorithms.category import keywords
from bot.convertor import save_to_json2

categorized = {cat: [] for cat in keywords.keys()}



async def sorting(data: dict, keywords):
    """"Алгоритм сортировки сообщений из не сортированого JSON file в сортированный"""
    default_category = {cat: [] for cat in data.keys()} 

    for msg in data.get("messages", []):
        msg_lower = msg.lower()
        found = False

        for k in keywords.keys():
            k = k.lower()
            if any(word in msg_lower for word in k): 
                    categorized[k].append(msg) 
                    found = True
                    
            if not found:
                default_category["uncategorized"].append((k, msg)) #TODO
    return await save_to_json2(categorized)
    

