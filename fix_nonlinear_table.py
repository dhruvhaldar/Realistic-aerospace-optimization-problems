import json
import glob

for filename in ["nonlinear.ipynb", "nonlinear_executed.ipynb"]:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        for cell in data["cells"]:
            if cell["cell_type"] == "code":
                for i, line in enumerate(cell["source"]):
                    if "md_table += \"| :--- | :--- | :--- |\\n\"" in line:
                        cell["source"][i] = line.replace("md_table += \"| :--- | :--- | :--- |\\n\"", "md_table += \"|---|---|---|\\n\"")
                        print(f"Updated in {filename}: {cell['source'][i]}")

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
