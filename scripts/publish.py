import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    for p in [ROOT / "dist", ROOT / "build"]:
        if p.exists():
            shutil.rmtree(p)
    for p in ROOT.glob("*.egg-info"):
        shutil.rmtree(p)
    for p in (ROOT / "src").glob("*.egg-info"):
        shutil.rmtree(p)

    subprocess.run(["uv", "run", "python", "-m", "build"], cwd=ROOT, check=True)
    subprocess.run(
        [
            "uv",
            "run",
            "python",
            "-m",
            "twine",
            "upload",
            "--config-file",
            ".pypirc",
            "--repository",
            "pypi",
            "dist/*",
        ],
        cwd=ROOT,
        check=True,
    )


if __name__ == "__main__":
    main()
