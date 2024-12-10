from typing import Optional
from random import choices
from string import ascii_uppercase


def random_code(size: Optional[int] = 16):
    code = choices(ascii_uppercase, k=size)

    return "".join(code)
