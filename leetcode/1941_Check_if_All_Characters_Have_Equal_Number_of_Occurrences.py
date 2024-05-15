from collections import Counter

def areOccurrencesEqual(s: str) -> bool:
    return len(set(Counter(s).values())) == 1