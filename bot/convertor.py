import os
import json
import asyncio
from algorithms.sorting_algorithm import sorting
from algorithms.category import category
from algorithms.export import export_to_txt


async def save_to_json(new_text: dict, filename: str = "messages.json"):
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump({"messages": []}, f, ensure_ascii=False, indent=4)

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for k, (under_category, v) in new_text.items():
       if k not in data:
            data[k] = []
       data[k].append((under_category, v))


    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return sorting(data, category)


async def save_to_json2(categorized: dict, filename: str = "sorting_messages.json"):
    """Beta version of message sorter хранителя"""


    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False, indent=4)

    # Загружаем текущие данные
    with open(filename, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}

   
    for k, (under_category, messages) in enumerate(categorized.items()):
        if (category or under_category) not in data:
            data[k] = [(under_category, messages)]  
        else:
            data[k].append((under_category, messages))

    # Сохраняем обратно в JSON
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return export_to_txt(data) #TODO