import asyncio
from algorithms.sorting_algorithm import sorting

# Мок-функция вместо save_to_json2
async def save_to_json2(data):
    return data

# Тестовые данные
test_data = {
    "messages": [
        "Ошибка доступа к диску",
        "Файл успешно сохранён",
        "Недостаточно прав для выполнения операции",
        "Процесс завершён без ошибок"
    ]
}

test_keywords = {
    "ошибка доступ": "диск",
    "недостаточно прав": "операция"
}

