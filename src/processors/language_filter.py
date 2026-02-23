def is_latin_script(text: str) -> bool:
    if not text:
        return False
    latin_count = sum(1 for char in text if char.isascii() or char.isspace())
    total_count = len(text)

    return (latin_count / total_count) >= 0.8