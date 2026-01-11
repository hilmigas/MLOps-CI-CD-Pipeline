def stable_hash(value: str) -> int:
    if not isinstance(value, str):
        raise TypeError("value must be a string")

    return sum(ord(c) for c in value) % 100
