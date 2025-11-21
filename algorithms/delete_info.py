import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import json
from category import category, under_category, text

async def delete(cmd):
    """Удаляет информацию из JSON файла на основе команды пользователя"""
    for cat in category:
        if cmd == cat:
            category.remove(cat)
            break
    
    for under_cat in under_category:
        if cmd == under_cat:
            under_category.remove(under_cat)
            break
    
    for txt in text:
        if cmd == txt:
            text.remove(txt)
            break