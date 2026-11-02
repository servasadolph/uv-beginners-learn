from main import greet


def test_greet_uses_default_name() -> None:
    assert greet() == "Hello, uv learner! Your uv project is working."


def test_greet_accepts_a_name() -> None:
    assert greet("Ada") == "Hello, Ada! Your uv project is working."
