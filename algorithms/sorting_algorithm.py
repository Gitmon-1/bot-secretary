import asyncio
from algorithms.category import keywords
from bot.convertor import save_to_json2


categorized = {cat: [] for cat in keywords.keys()}


async def sorting(data: dict, keywords):
    """"Алгоритм сортировки сообщений из не сортированого JSON file в сортированный"""
    default_category = {cat: [] for cat in data.keys()} 

    for k, (under_category, msg) in enumerate(data.items()):
        msg_lower = msg.lower()
        found = False

        for keys in keywords.keys():
            keys = keys.lower()
            if any(word in msg_lower for word in keys.split()): 
                    categorized[k].append((under_category, msg)) 
                    found = True
                    break

            if keys == k:
                categorized[k].append((under_category, msg))
                found = True
                break
                    
            if not found:
                default_category["uncategorized"].append((k, under_category, msg)) #TODO
    return await save_to_json2(categorized)
    

