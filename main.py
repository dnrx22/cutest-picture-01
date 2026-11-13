"""Copy the bundled picture to the grader's output directory.

The entry ships one image, entry.png, next to this script. Running the
program writes that exact file, byte for byte, to entry.png inside the
output directory. The output directory comes from MAKEFUN_OUTPUT_DIR
and defaults to /output. The copy is pure and deterministic: two runs
always write identical bytes.
"""

import os
import shutil
from pathlib import Path


def main():
    source = Path(__file__).resolve().parent / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"bundled picture missing: {source}")
    if source.stat().st_size == 0:
        raise ValueError(f"bundled picture is empty: {source}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()
