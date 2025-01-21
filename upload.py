import dtlpy as dl
import os

dl.setenv("prod")
dataset = dl.datasets.get(dataset_id="678641e4c1f76e442775afa6")

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
            "system": {"shebang": {"dltype": "evaluation-studio"}, 
                       "evaluation": {"layoutName": folder}}
        },
    )
    print(data_item)
