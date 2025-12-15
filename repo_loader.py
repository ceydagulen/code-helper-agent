from pathlib import Path


def load_repo(repo_path: str):
    files = []

    for path in Path(repo_path).rglob("*.py"):
        try:
            content = path.read_text(encoding="utf-8")
            files.append({
                "path": str(path),
                "content": content
            })
        except Exception:
            pass

    return files
