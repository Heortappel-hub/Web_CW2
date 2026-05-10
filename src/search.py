import json
import os

INDEX_FILE = "data/index.json"

# ===== Index persistence =====

def save_index(index, path=INDEX_FILE):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    print(f"Index saved to {path}")


def load_index(path=INDEX_FILE):
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Index file not found at {path}. Run 'build' first."
        )
    with open(path, "r", encoding="utf-8") as f:
        index = json.load(f)
    print(f"Index loaded from {path} ({len(index)} unique words)")
    return index