def validate_keys(data, required_keys):
    """
    Validate that all required keys exist.
    """
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")

    return True