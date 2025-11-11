import os
import json
import asyncio
from algorithms.sorting_algorithm import sorting
from algorithms.category import keywords
from algorithms.export import export_to_txt


async def save_to_json(new_text: dict, filename: str = "messages.json"):
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump({"messages": []}, f, ensure_ascii=False, indent=4)

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for k, v in new_text.items():
       if k not in data:
            data[k] = []
       data[k].append(v)


    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return sorting(data, keywords=keywords)


async def save_to_json2(categorized: dict, filename: str = "sorting_messages.json"):
    """Beta version of message sorter хранителя"""

    # Если файл не существует — создаём базовую структуру
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False, indent=4)

    # Загружаем текущие данные
    with open(filename, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}

    # Объединяем старые и новые категории
    for category, messages in categorized.items():
        if category not in data:
            data[category] = []  
        for msg in messages:
            if msg not in data[category]:  
                data[category].append(msg)

    # Сохраняем обратно в JSON
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return export_to_txt(data) #TODO