import re

def tokenize(text):

    text = text.lower()
    tokens = re.findall(r"[a-z0-9']+", text)
    return tokens


def build_index(pages):
    
    index = {}
    
    for url, text in pages.items():
        tokens = tokenize(text)

        for position, word in enumerate(tokens):
            # Ensure the word exists in the outer dict
            if word not in index:
                index[word] = {}

            # Ensure this URL exists in the inner dict
            if url not in index[word]:
                index[word][url] = []

            # Record the position
            index[word][url].append(position)

    return index