import dtlpy as dl
import json
import os


with open("examples/index.json", "w") as f:
    examples = [d for d in os.listdir("examples") if os.path.isdir(f"examples/{d}")]
    f.write(json.dumps(examples))

dl.setenv("prod")
dataset = dl.datasets.get(dataset_id="67b1d53aa697b09dd00831b9")

binaries_dataset = dataset.project.datasets._get_binaries_dataset()

for folder in os.listdir("examples"):
    if not os.path.isdir(f"examples/{folder}"):
        continue
    
    _ = binaries_dataset.items.upload(
        local_path=f"examples/{folder}/*",
        remote_path=f"/.dataloop/evaluation-studio-layouts/{folder}",
        overwrite=True,
    )
    

    data_item = dataset.items.upload(
        local_path=f"examples/{folder}/{folder}-data.json",
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
