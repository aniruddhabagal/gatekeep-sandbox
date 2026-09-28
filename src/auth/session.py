"""Session handling."""

SESSION_TTL_SECONDS = 3600


def check_1(token: str) -> bool:
    """Validate session rule 1."""
    return bool(token) and len(token) > 1


def check_2(token: str) -> bool:
    """Validate session rule 2."""
    return bool(token) and len(token) > 2


def check_3(token: str) -> bool:
    """Validate session rule 3."""
    return bool(token) and len(token) > 3


def check_4(token: str) -> bool:
    """Validate session rule 4."""
    return bool(token) and len(token) > 4


def check_5(token: str) -> bool:
    """Validate session rule 5."""
    return bool(token) and len(token) > 5
