import dtlpy as dl
import json
import os


with open("examples/index.json", "w") as f:
    examples = [d for d in os.listdir("examples") if os.path.isdir(f"examples/{d}")]
    f.write(json.dumps(examples))

dl.setenv("rc")
dataset = dl.datasets.get(dataset_id="67b465a6be6c2c1a9e682ee2")

binaries_dataset = dataset.project.datasets._get_binaries_dataset()

for folder in os.listdir("examples"):
    if not os.path.isdir(f"examples/{folder}"):
        continue
    layout_item = binaries_dataset.items.upload(
        local_path=f"examples/{folder}/form-schema.json",
        remote_path=f"/.dataloop/evaluation-studio-layouts",
        remote_name=f"{folder}.json",
        overwrite=True,
    )

    data_item = dataset.items.upload(
        local_path=f"examples/{folder}/item.json",
        remote_name=f"{folder}-example.json",
        overwrite=True,
        item_metadata={
            "system": {
                "shebang": {"dltype": "evaluation-studio"},
                "evaluation": {"layoutName": folder},
            }
        },
    )
    print(data_item)
