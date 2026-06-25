from typer import Typer

# PYTHONPATH=src is set via .env (copied from .env.example by scripts/setup)

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


@cmd.command()
def version():
    from my_sdk.version import __version__

    print(__version__)


if __name__ == "__main__":
    cmd()
