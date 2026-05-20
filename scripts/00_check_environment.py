"""Check the public benchmark environment."""

from importlib import import_module

REQUIRED = {
    "pandas": "2.2.0",
    "numpy": "1.26.0",
    "sklearn": "1.5.0",
    "geopandas": "0.14.4",
    "shapely": "2.0.4",
    "h3": "4.4.2",
    "xgboost": "2.1.0",
    "matplotlib": "",
    "openpyxl": "",
}


def main() -> int:
    failed = False
    for module, expected in REQUIRED.items():
        try:
            imported = import_module(module)
            version = getattr(imported, "__version__", "installed")
            suffix = f" expected {expected}" if expected else ""
            print(f"OK {module}: {version}{suffix}")
        except Exception as exc:
            failed = True
            print(f"MISSING {module}: {exc}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
