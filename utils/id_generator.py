import uuid
import secrets


def generate_uuid() -> str:
    """
    generate uniq id (UUID4).
    Example: '550e8400-e29b-41d4-a716-446655440000'
    For DB fils
    """
    return str(uuid.uuid4())


def generate_short_id(length: int = 8) -> str:
    """
    length: get Int count of return symbols
    (optional) generate short ID.
    Example: 'a3f8b9d2'
    For JSON files to get names short and visual friendly
    """
    # secrets.token_hex create str, there every byte equals 2 symbols,
    # that's why divide to 2
    return secrets.token_hex(length // 2)
