"""A tiny project you can run with ``uv run main.py``."""


def greet(name: str = "uv learner") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}! Your uv project is working."


if __name__ == "__main__":
    print(greet())
