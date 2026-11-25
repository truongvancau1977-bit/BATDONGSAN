import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "knowledge.js")

PROJECTS = {
    "than_linh": {
        "name": "Dự án BĐS Thần Lĩnh (Nghệ An)",
        "path": os.path.join(BASE_DIR, "QUẢN LÝ DỰ ÁN BĐS THẦN LĨNH", "HO_SO_DU_LIEU_DU_AN_THAN_LINH.md"),
    },
    "dong_binh_duong": {
        "name": "Dự án BĐS Đông Bình Dương",
        "path": os.path.join(BASE_DIR, "QUẢN LÝ DỰ ÁN BĐS ĐÔNG BÌNH DƯƠNG", "HO_SO_DU_LIEU_DU_AN_DONG_BINH_DUONG.md"),
    },
    "hc_signature": {
        "name": "Dự án CC HC Signature Tower",
        "path": os.path.join(BASE_DIR, "DỤ ÁN CC HC SIGNATURE", "HO_SO_DU_LIEU_DU_AN_HC_SIGNATURE.md"),
    },
}

data = {}
for key, info in PROJECTS.items():
    if os.path.exists(info["path"]):
        with open(info["path"], "r", encoding="utf-8") as f:
            data[key] = {
                "name": info["name"],
                "content": f.read()
            }
            print(f"[OK] Loaded {key}: {len(data[key]['content'])} chars")
    else:
        print(f"[SKIP] Not found: {info['path']}")

with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write("window.PROJECT_KNOWLEDGE = ")
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Generated {OUT_FILE} successfully.")
