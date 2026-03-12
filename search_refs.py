import json
import glob

for filename in glob.glob("*.ipynb"):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        for cell in data["cells"]:
            if cell["cell_type"] == "markdown":
                for line in cell["source"]:
                    if "Reference" in line or "Available at" in line:
                        print(f"Found in {filename}: {line}")
