import os
import json
def save_to_json(new_text: str, filename: str = "messages.json"):
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump({"messages": []}, f, ensure_ascii=False, indent=4)

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    data["messages"].append(new_text)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)