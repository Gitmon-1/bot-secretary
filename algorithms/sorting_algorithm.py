import asyncio
import json
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from algorithms.category import catalog, keywords

categorized = {cat: [] for cat in keywords.keys()}


async def sorting(data: dict, catalog):
    """"Алгоритм сортировки сообщений из не сортированого JSON file в сортированный"""

    for msg in data.get("messages", []):
        msg_lower = msg.lower()
        found = False

        for k, v in keywords.items():
            if any(word in msg_lower for word in v): #если слово из ключевых слов есть в сообщении
                    categorized[k].append(msg) #почкему добавляем по значению ключа, а не по ключу?
                    found = True
                    
            if not found:
                return
    return categorized
    

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