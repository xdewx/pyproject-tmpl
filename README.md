# pyproject-tmpl

## features

1. uv — package & project manager
2. pytest & pytest-cov
3. pre-commit
4. darker for code format
5. ruff for lint
6. commitlint for commit message format
7. typer for cli
8. sqlmodel for database ORM
9. alembic for database migration

## introduction

the project uses `src-layout`, includes `my_sdk` (for publish) and `biz` (for business logic).

feel free to rename `my_sdk` to `[the name you want]` in the whole project for your own use or publish.

### dev

before you start:

1. must run `uv run scripts/setup.py` — this creates `.env` (with `PYTHONPATH=src`) and installs dependencies & git hooks
2. replace `my_sdk` with `[the name you want]` in the whole project

### unit test

`uv run -m pytest`
> `htmlcov` folder contains html coverage report.

### run cli

`uv run main.py --help`

### release sdk

1. `cp .pypirc.example .pypirc`
2. replace your token in `.pypirc`
3. `git tag vx.y.z`
4. `uv run scripts/publish.py`

### build executable file

`uv run scripts/build.py`
