def stable_hash(value: str) -> int:
    return sum(ord(c) for c in value) % 100