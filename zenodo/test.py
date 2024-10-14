import zenodopy
import os
import time 
import json


version_tag = os.getenv("VERSION_TAG")

print("my msg")
print(version_tag)
# zenodo_token = os.getenv("ZENODO_TOKEN")


def update_version_in_zenodo(file_path, new_version):
    with open(file_path, "r") as file:
        zenodo_data = json.load(file)

    zenodo_data["metadata"]["version"] = new_version

    with open(file_path, "w") as file:
        json.dump(zenodo_data, file, indent=2)


zenodo_file_path = "/home/runner/work/solver-benchmark/solver-benchmark/zenodo/.zenodo.json"

update_version_in_zenodo(zenodo_file_path, version_tag)

max_retries = 5

for attempt in range(1, max_retries + 1):
    try:

        zeno = zenodopy.Client(
            sandbox=True,
            token="CNXNk6GBg0dQUvZJsCUEajG4ZZnAr8YUrWPR9oCucnu8vq39jFJDUGoYW6WK",
        )

        zeno.set_project(dep_id=106299)

        zeno.update(
            source="/home/runner/work/solver-benchmark/solver-benchmark/benchmarks/",
            publish=True,
            metadata_json="/home/runner/work/solver-benchmark/solver-benchmark/zenodo/.zenodo.json",
        )
        print("Update succeeded.")
        break  

    except Exception as e:
        print(f"Attempt {attempt} failed with error: {e}")

        time.sleep(2)  # Optional: Wait before retrying

        zeno._delete_project(dep_id=106299)

        if attempt == max_retries:
            print("Max retries reached. Exiting.")
            raise 
        else:
            time.sleep(2) 
