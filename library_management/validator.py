def validate_text(value: str, field_name: str) -> str:
    """Validate that text is not empty."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} cannot be empty.")
    return value.strip()


def validate_positive_number(value: float, field_name: str) -> float:
    """Validate that a number is greater than zero."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field_name} must be a number.")

    if value <= 0:
        raise ValueError(f"{field_name} must be greater than zero.")

    return value


def validate_non_negative_number(value: float, field_name: str) -> float:
    """Validate that a number is zero or greater."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field_name} must be a number.")

    if value < 0:
        raise ValueError(f"{field_name} cannot be negative.")

    return value