#!/usr/bin/env python3
# spell_check.py
"""
Simple spell checker backends.

Usage (example):
    python3 spell_check.py -s /path/to/dict.txt < text_with_words_to_check

Backends:
  -l : list-backed (linear search)
  -s : set-backed (fast)
  -d : dict-backed (fast)
"""

import sys

WORDS_PATH = "/usr/share/dict/words"

class WordsList:
    def __init__(self, path=WORDS_PATH):
        self.data = []
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    w = line.strip()
                    if w:
                        self.data.append(w)
        except FileNotFoundError:
            raise FileNotFoundError(f"Dictionary file not found: {path}")

    def __contains__(self, target):
        return target in self.data

class WordsSet:
    def __init__(self, path=WORDS_PATH):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                self.data = set(w.strip() for w in f if w.strip())
        except FileNotFoundError:
            raise FileNotFoundError(f"Dictionary file not found: {path}")

    def __contains__(self, target):
        return target in self.data

class WordsDict:
    def __init__(self, path=WORDS_PATH):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                self.data = {w.strip(): True for w in f if w.strip()}
        except FileNotFoundError:
            raise FileNotFoundError(f"Dictionary file not found: {path}")

    def __contains__(self, target):
        return target in self.data

# map flags to classes
WORDS_DATABASES = {"-l": WordsList, "-s": WordsSet, "-d": WordsDict}

def main(argv=None, stdin=None):
    if argv is None:
        argv = sys.argv[1:]
    if stdin is None:
        stdin = sys.stdin

    if not argv:
        print("Usage: spell_check.py [-l|-s|-d] [dict_path]", file=sys.stderr)
        sys.exit(2)

    mode = argv[0]
    path = argv[1] if len(argv) > 1 else WORDS_PATH

    if mode not in WORDS_DATABASES:
        print("Invalid mode. Choose one of -l, -s, -d", file=sys.stderr)
        sys.exit(2)

    db = WORDS_DATABASES[mode](path)

    # For each token on stdin, if token not in dictionary, print it (misspell)
    for line in stdin:
        tokens = line.strip().split()
        for token in tokens:
            if token and token not in db:
                print(token)

if __name__ == "__main__":
    main()
