import json
import os

MEMORY_FILE = "memory.json"
# Ensure the memory file exists in the current directory

def load_user_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except Exception:
        # If file is corrupted or empty, return empty dict
        return {}

def save_user_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def update_user(memory, user_id, user_input, bot_response, emotion, polarity):
    if user_id not in memory:
        memory[user_id] = []
    memory[user_id].append({
        "user_input": user_input,
        "bot_response": bot_response,
        "emotion": emotion,
        "polarity": polarity
    })
    save_user_memory(memory)

