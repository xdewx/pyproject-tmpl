import sys
from pathlib import Path

from typer import Typer

# TODO: i don't want to add this manually, but i have no idea how to do it automatically at present
sys.path.append(str(Path(__file__).parent / "src"))

print(sys.path)

cmd = Typer()


@cmd.command()
def sub(a: int, b: int) -> int:
    c = a - b
    print(f"sub({a}, {b}) = {c}")
    return c


@cmd.command()
def setup_db():
    from conf import setup_database

    # if you need to use database, invoke setup_database freely
    setup_database()


if __name__ == "__main__":
    cmd()
