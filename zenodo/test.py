import zenodopy
import os

version_tag = os.getenv("VERSION_TAG")

print("my msg")
print(version_tag)
# zenodo_token = os.getenv("ZENODO_TOKEN")

zeno = zenodopy.Client(
    sandbox=True, token="CNXNk6GBg0dQUvZJsCUEajG4ZZnAr8YUrWPR9oCucnu8vq39jFJDUGoYW6WK"
)

# zeno.list_projects

# zeno.create_project(
#     title="twoversion11",
#     upload_type="other",
#     metadata_json="zenodo/.zenodo.json",
# )

# print(zeno.deposition_id)

zeno.set_project(dep_id=101526)


# upload file to zenodo
# zeno.upload_file("zenodo/.zenodo.json", publish=True)
zeno.update(
    source="/home/zenodo",
    publish=True,
    metadata_json="zenodo/.zenodo.json",
)
# zeno.list_files()
# zeno.upload_file("test.file.txt",publish=True)


# zeno.change_metadata(title="my test file",
#                         upload_type="text",
#                         description="Eu reprehenderit non et mollit excepteur nisi laborum labore sit ex ipsum ullamco id. Aute qui fugiat in aute. In quis aute enim cupidatat laborum qui voluptate anim Lorem nulla sint do.",
#                         creator="akshat")
# list project id's associated to zenodo account
