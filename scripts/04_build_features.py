"""Public benchmark pipeline stage: lag and contextual feature construction.

This wrapper is intentionally conservative. Raw municipal datasets are not
redistributed in this repository, so full raw-data reproduction requires placing
the source files described in data_sources/download_instructions.md under data/raw/.
"""

from pathlib import Path
import sys


REQUIRED_INPUTS = ['data/processed/fase4_integrated/monthly/CDMX_monthly_train.parquet']


def main() -> int:
    missing = [p for p in REQUIRED_INPUTS if not Path(p).exists()]
    if missing:
        print("04_build_features.py: raw/intermediate inputs are not available in this public package.")
        print("This is expected when cloning the artifact-only repository.")
        print("Download the original public datasets and follow data_sources/download_instructions.md.")
        print("Missing inputs:")
        for item in missing:
            print(f"  - {item}")
        return 2
    print("04_build_features.py: required inputs found. Insert project-specific execution here or run the audited notebooks/scripts from the full thesis workspace.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
