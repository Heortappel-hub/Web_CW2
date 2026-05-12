## Overview

This tool implements a complete search engine pipeline:

1. **Crawler** — BFS-based web crawler that traverses the target site.
2. **Indexer** — builds an inverted index `{word: {url: [positions]}}` from crawled pages, recording both frequency and position for each word in each page.
3. **Search** — supports inspecting the index for a single word (`print`) and finding pages containing one or more words (`find`).

The tool is operated through an interactive shell with four commands: `build`, `load`, `print`, and `find`.

## Installation

Clone the repository:

```bash
git clone https://github.com/Heortappel-hub/Web_CW2.git
cd Web_CW2
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Start the interactive shell from the project root:

```bash
python src/main.py
```

You'll see a `>` prompt. The tool supports four commands.

### build: Crawl and build the index

### load: load indexes from exist json file

### print <word>: 
Inspect the index for a word
example: print good

### find <word1> <word2>...: 
Find all pages that include the input words, split by space.
example: find indifferent
example2: find good friends

## Test
Mock Test:
The test uses mocked unittests instead of real requests.

Running:
Run the following command in the project root directory.
> python -m unittest discover tests -v


