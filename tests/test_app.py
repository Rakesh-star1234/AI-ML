from basic_project.app import greet


def test_greet_default() -> None:
    assert greet() == "Hello, World!"


def test_greet_custom_name() -> None:
    assert greet("Python") == "Hello, Python!"
