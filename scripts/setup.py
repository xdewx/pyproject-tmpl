import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    env_example = ROOT / ".env.example"
    env = ROOT / ".env"
    if env_example.exists() and not env.exists():
        shutil.copy(env_example, env)

    subprocess.run(
        ["uv", "sync", "--all-extras", "--index-strategy", "unsafe-best-match"],
        cwd=ROOT,
        check=True,
    )

    hooks_dir = ROOT / ".git" / "hooks"
    if not (hooks_dir / "pre-commit").exists():
        subprocess.run(["pre-commit", "install"], cwd=ROOT, check=True)
    if not (hooks_dir / "commit-msg").exists():
        subprocess.run(
            ["pre-commit", "install", "--hook-type", "commit-msg"], cwd=ROOT, check=True
        )


if __name__ == "__main__":
    main()
