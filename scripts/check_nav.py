"""Sanity check: parse mkdocs.yml and verify all nav-referenced docs exist."""
import pathlib
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"


def walk(item, missing):
    if isinstance(item, dict):
        for v in item.values():
            walk(v, missing)
    elif isinstance(item, list):
        for x in item:
            walk(x, missing)
    elif isinstance(item, str) and item.endswith(".md"):
        if not (DOCS / item).exists():
            missing.append(item)


def main() -> int:
    # mkdocs.yml uses !!python tags etc. – use unsafe_load? Actually it's plain YAML.
    # mkdocs YAML can include custom tags; try safe_load first, fall back.
    text = (ROOT / "mkdocs.yml").read_text()
    try:
        y = yaml.safe_load(text)
    except yaml.YAMLError:
        y = yaml.unsafe_load(text)
    missing = []
    walk(y.get("nav", []), missing)
    print(f"missing files: {len(missing)}")
    for m in missing:
        print(f"  {m}")
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
