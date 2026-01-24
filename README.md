# pyproject-tmpl

## features

1. pytest
2. pre-commit
3. darker for code format
4. ruff for lint
5. commitlint for commit message format
6. typer for cli
7. sqlmodel for database ORM
8. alembic for database migration

## introduction

the project uses `src-layout`, includes `my_sdk` (for publish) and `biz` (for business logic).

~~`sdk` is designed for publish and no need to rename, we use file/folder mapping `my_sdk=src/sdk` in `pyproject.toml`.~~

feel free to rename `my_sdk` to `[the name you want]` in the whole project for your own use or publish.

### dev

before you start:

1. must run `./scripts/setup`
1. replace `my_sdk` with `[the name you want]` in the whole project
1. ~~remember to `uv pip install -e .[all]` to make sure `my_sdk` is available in development.~~

### unit test

`uv run -m pytest`

### run cli

`uv run main.py --help`

### release sdk

1. `cp .pypirc.example .pypirc`
2. replace your token in `.pypirc`
3. `git tag vx.y.z`
4. `./scripts/publish`

### build executable file

`./scripts/build`
