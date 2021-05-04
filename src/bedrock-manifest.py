import json
from pathlib import Path
from requests import get

def generateManifests():
    # get uuids
    uuid_list = []
    for item in get("https://www.uuidgenerator.net/api/version4/4").iter_lines():
        uuid_list.append(item.decode("utf-8"))

    # resource pack
    pack_path = Path("resource_packs", "TEST_RP")
    default = json.load(open("rp_manifest.json", "r"))
    if not pack_path.exists():
        pack_path.mkdir(parents=True)

    default["header"]["uuid"] = uuid_list[0]
    default["modules"][0]["uuid"] = uuid_list[1]

    with Path(pack_path, "manifest.json").open() as f:
        f.write(json.dumps(default))

    # behavior pack
    pack_path = Path("behavior_packs", "TEST_BP")
    default = json.load(open("bp_manifest.json", "r"))
    if not pack_path.exists():
        pack_path.mkdir(parents=True)

    default["header"]["uuid"] = uuid_list[2]
    default["modules"][0]["uuid"] = uuid_list[3]
    default["dependencies"][0]["uuid"] = uuid_list[0]

    with Path(pack_path, "manifest.json").open() as f:
        f.write(json.dumps(default))

if __name__ == "__main__":
    generateManifests()