import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    for p in [ROOT / "dist", ROOT / "build"]:
        if p.exists():
            shutil.rmtree(p)

    subprocess.run(["uv", "run", "pyinstaller", "main.spec"], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
