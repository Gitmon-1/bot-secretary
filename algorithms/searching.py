import asyncio
from algorithms.sorting_algorithm import sorting
import requests


def find(keyword: str, data: dict) -> str:
    """Ищет сообщения, содержащие ключевое слово, и возвращает их в виде строки."""
    
