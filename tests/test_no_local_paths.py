from pathlib import Path


TEXT_SUFFIXES = {".md", ".txt", ".py", ".csv", ".yml", ".yaml", ".cff", ".json"}
FORBIDDEN = [
    "C:" + "\\" + "Users" + "\\",
    "C:" + "\\" + "Proyectos" + "\\",
    "OneDrive - " + "Instituto Politecnico Nacional",
]


def test_no_local_paths_in_text_files():
    for path in Path(".").rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            text = path.read_text(encoding="utf-8", errors="ignore")
            for needle in FORBIDDEN:
                assert needle not in text, f"{needle} found in {path}"
