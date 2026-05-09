import indexer
import crawler

if __name__ == "__main__":
    print("Crawling...")
    pages = crawler.crawl()
    print(f"Got {len(pages)} pages\n")

    print("Building index...")
    index = indexer.build_index(pages)
    print(f"Index has {len(index)} unique words\n")

    # Inspect a specific word
    word = "good"
    if word in index:
        print(f"'{word}' appears in {len(index[word])} pages:")
        for url, positions in index[word].items():
            print(f"  {url}: {len(positions)} times at positions {positions[:5]}...")
    else:
        print(f"'{word}' not found in index")