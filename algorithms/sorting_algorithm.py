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
#Алгоритм имеет несколько проблем. Первая: он итерируется до первого совпадения в ключевых словах. Хотя самих сообщений может быть несколько.
#Во вторых объем файла и состояние не очищаются, а стоновятся только больше.
    for k, v in keywords.items():
        if any(word in msg_lower for word in k):
                categorized[v].append(msg) #он добавляет не к категории, а к ключевому слову сообщение.
                found = True
                break #TODO
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
            data[category] = []  # создаём новую категорию, если её не было
        for msg in messages:
            if msg not in data[category]:  # избегаем дублей
                data[category].append(msg)

    # Сохраняем обратно в JSON
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)