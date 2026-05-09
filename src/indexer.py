import re

def tokenize(text):
    # Use regular expressions to split the text into words
    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens

def build_index(documents):
    index = {}
    for doc_id, text in enumerate(documents):
        tokens = tokenize(text)
        for token in tokens:
            if token not in index:
                index[token] = set()
            index[token].add(doc_id)
    return index