import os


def clear() -> None:
    system: str = os.name
    if system == "nt":
        os.system("cls")
    else:
        os.system("clear")
