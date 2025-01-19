import re

def nums(s: str) -> list[int]:
    return list(map(int, re.findall(r'\d+', s)))