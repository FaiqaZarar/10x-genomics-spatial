"""
Fix: 'state' key missing from metadata.widgets in Jupyter notebooks.
Run this script from the root of your 10x-genomics-spatial repo folder.
"""

import json
import glob
import os

notebooks = [
    "01_scanpy_basic/01_scanpy_basic_spatial.ipynb",
    "02_squidpy_visium_fluo/02_visium_fluorescence.ipynb",
    "03_squidpy_visium_hne/03_visium_hne.ipynb",
    "04_squidpy_xenium/04_xenium.ipynb",
]

for path in notebooks:
    if not os.path.exists(path):
        print(f"  SKIPPED (not found): {path}")
        continue

    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    metadata = nb.get("metadata", {})
    widgets = metadata.get("widgets", None)

    if widgets is not None and "state" not in widgets:
        nb["metadata"]["widgets"] = {"state": {}, "version_major": 2, "version_minor": 0}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        print(f"  FIXED: {path}")
    elif widgets is None:
        print(f"  OK (no widgets metadata): {path}")
    else:
        print(f"  OK (already has state): {path}")

print("\nDone! Now commit and push the fixed notebooks to GitHub.")
