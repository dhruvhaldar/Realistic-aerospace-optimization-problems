import json
import glob

for filename in ["b747_pitch_tracking.ipynb", "b747_pitch_tracking_executed.ipynb"]:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        for cell in data["cells"]:
            if cell["cell_type"] == "markdown":
                for i, line in enumerate(cell["source"]):
                    if "> **Reference:** Chrif, L., Kadda, Z. M., & Mohammed, L. (2020)." in line:
                        cell["source"][i] = line.replace("> **Reference:**", "> **Reference:** ").replace("Available at", "> [Download PDF](")
                        print(f"Updated in {filename}: {cell['source'][i]}")

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
