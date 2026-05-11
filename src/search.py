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

def print_word(index, word):
    word = word.lower()
    if word not in index:
        print(f"'{word}' not found in index")
        return
    entry = index[word]
    print(f"'{word}' appears in {len(entry)} page(s):")
    for url, positions in entry.items():
        print(f"  {url}")
        print(f"    frequency: {len(positions)}, positions: {positions}")
        
def find_pages(index, words):
    words = [w.lower() for w in words]
    for word in words:
        if word not in index:
            print(f"No pages found ('{word}' is not in the index)")
            return

    url_sets = [set(index[word].keys()) for word in words]
    result = set.intersection(*url_sets)

    if not result:
        print("No pages contain all the given words")
        return

    print(f"Found {len(result)} page(s) containing {words}:")
    for url in sorted(result):
        print(f"  {url}")