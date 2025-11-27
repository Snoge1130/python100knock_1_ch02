"""
User greeting module.

This module provides simple greeting functionality.
"""


def greet(name: str = "World") -> str:
    """
    Generate a greeting message for the given name.

    Args:
        name: The name to greet. Defaults to "World".

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
