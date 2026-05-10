from crawler import crawl
from indexer import build_index
from search import save_index, load_index


def cmd_build():
    """Crawl, build index, and save to disk."""
    print("Starting crawl...")
    pages = crawl()   # Crawl website pages and collect text
    print(f"Crawled {len(pages)} pages\n")

    print("Building index...")
    index = build_index(pages)   # Convert documents into inverted index
    print(f"Index has {len(index)} unique words\n")

    save_index(index)   # Persist index for later loading


def cmd_load():
    """Load index from disk."""
    return load_index()


def main():
    index = None

    while True:
        try:
            line = input("> ").strip()   # Read CLI command from user
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not line:
            continue

        parts = line.split()
        cmd = parts[0].lower()

        try:
            # Dispatch user commands to search engine functions
            if cmd == "build":
                cmd_build()
            elif cmd == "load":
                index = cmd_load()
            elif cmd == "print":
                if len(parts) < 2:
                    print("Usage: print <word>")
                else:
                    cmd_print(index, parts[1])
            elif cmd == "find":
                if len(parts) < 2:
                    print("Usage: find <word> [word ...]")
                else:
                    cmd_find(index, parts[1:])
            elif cmd in ("exit", "quit"):
                break
            else:
                print(f"Unknown command: {cmd}")

        # Handle file and runtime errors to fix unexpected crashes
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    print("Commands: build, load, print <word>, find <word> [word ...], exit")
    main()