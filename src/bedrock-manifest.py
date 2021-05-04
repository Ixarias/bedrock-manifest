import json
import os
from pathlib import Path
from uuid import uuid4

behavior_manifest = {
    "format_version": 2,
    "header": {
        "description": "pack.description",
        "name": "pack.name",
        "uuid": "",
        "version": [0, 0, 1],
        "min_engine_version": [1, 16, 220]
    },
    "modules": [
        {
            "type": "data",
            "uuid": "",
            "version": [0, 0, 1]
        }
    ],
    "dependencies": [
        {
            "uuid": "",
            "version": [0, 0, 1]
        }
    ]
}

resource_manifest = {
    "format_version": 2,
    "header": {
        "description": "pack.description",
        "name": "pack.name",
        "uuid": "",
        "version": [0, 0, 1],
        "min_engine_version": [1, 16, 200]
    },
    "modules": [
        {
            "type": "resources",
            "uuid": "",
            "version": [0, 0, 1]
        }
    ]
}

languages = [
    "en_US"
]

en_US = """
        pack.name = Example Pack
        pack.description = Example Pack Description
        """

def generateManifests():

    uuid_list = []
    for i in range(4):
        uuid_list.append(str(uuid4()))

    # resource pack
    pack_path = Path("resource_packs", "TEST_RP")
    if not Path(pack_path, "texts").exists():
        Path(pack_path, "texts").mkdir(parents=True, exist_ok=True)

    resource_manifest["header"]["uuid"] = uuid_list[0]
    resource_manifest["modules"][0]["uuid"] = uuid_list[1]


    with Path(pack_path, "manifest.json").open(mode="w") as f:
        f.write(json.dumps(resource_manifest))
    with Path(pack_path, "texts", "languages.json").open(mode="w") as f:
        f.write(json.dumps(languages))
    with Path(pack_path, "texts", "en_US.lang").open(mode="w") as f:
        f.write(en_US)

    with open("world_resource_packs.json", "w") as rpacks:
        json.dump([{
            "pack_id": uuid_list[0],
            "version": [0, 0, 1]
        }], rpacks)

    # behavior pack
    pack_path = Path("behavior_packs", "TEST_BP")
    if not Path(pack_path, "texts").exists():
        Path(pack_path, "texts").mkdir(parents=True, exist_ok=True)

    behavior_manifest["header"]["uuid"] = uuid_list[2]
    behavior_manifest["modules"][0]["uuid"] = uuid_list[3]
    behavior_manifest["dependencies"][0]["uuid"] = uuid_list[0]


    with Path(pack_path, "manifest.json").open(mode="w") as f:
        f.write(json.dumps(behavior_manifest))
    with Path(pack_path, "texts", "languages.json").open(mode="w") as f:
        f.write(json.dumps(languages))
    with Path(pack_path, "texts", "en_US.lang").open(mode="w") as f:
        f.write(en_US)

    with open("world_behavior_packs.json", "w") as bpacks:
        json.dump([{
            "pack_id": uuid_list[2],
            "version": [0, 0, 1]
        }], bpacks)

if __name__ == "__main__":
    generateManifests()