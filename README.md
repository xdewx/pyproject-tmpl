# pyproject-tmpl

## features

1. pytest
2. pre-commit
3. darker for code format
4. ruff for lint
5. commitlint for commit message format
6. typer for cli

## 使用方式

- 初始化环境：
    `./scripts/setup`

- 执行测试：
    `uv run -m pytest`

- 运行cli：
    `uv run main.py --help`

- 构建发布：
    1. `cp .pypirc.example .pypirc`
    2. replace your token in .pypirc
    3. `git tag vx.y.z`
    4. `./scripts/publish`

- 构建可执行文件：
    `./scripts/build`
