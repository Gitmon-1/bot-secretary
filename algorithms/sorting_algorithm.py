import asyncio
from algorithms.category import category, under_category
from bot.convertor import save_to_json2


categorized = {cat: [] for cat in category}


async def sorting(data: dict, category):
    """"Алгоритм сортировки сообщений из не сортированого JSON file в сортированный"""
    default_category = {cat: [] for cat in data.keys()} 

    for k, (under_category, msg) in enumerate(data.items()):
        msg_lower = msg.lower()
        found = False

        for keys in category:
            keys = keys.lower()

            if keys == k:
                categorized[k].append((under_category, msg))
                found = True
                break

                    
            if not found:
                default_category["uncategorized"].append((k, under_category, msg)) #TODO
    return await save_to_json2(categorized)
    

