from crawler import crawl
from indexer import build_index
from search import save_index, load_index


def cmd_build():
    """Crawl, build index, and save to disk."""
    print("Starting crawl...")
    pages = crawl()
    print(f"Crawled {len(pages)} pages\n")

    print("Building index...")
    index = build_index(pages)
    print(f"Index has {len(index)} unique words\n")

    save_index(index)


def cmd_load():
    """Load index from disk."""
    return load_index()


def main():
    """Read commands from the user in a shell-like loop."""
    index = None

    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not line:
            continue

        parts = line.split()
        cmd = parts[0].lower()
        args = parts[1:]

        if cmd == "build":
            cmd_build()
        elif cmd == "load":
            index = cmd_load()
        elif cmd == "print":
            print("(print command — to be implemented)")
        elif cmd == "find":
            print("(find command — to be implemented)")
        elif cmd in ("exit", "quit"):
            break
        else:
            print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()