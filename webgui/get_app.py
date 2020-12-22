from os import mkdir
from os.path import isdir
from requests import get
from json import loads


def getapp(name, url):

    if not isdir("apps"):
        mkdir("apps")

    try:
        res = get(url)
    except Exception as exc:
        print(f"ERROR: Humbackfile.json downloading error: {exc}")
        return False

    try:
        res.raise_for_status()
    except Exception as exc:
        print(f"ERROR: Humbackfile.json downloading error: {exc}")
        return False

    humbackfile = loads(res.text)

    if not isdir("apps/{0}".format(name)):
        mkdir("apps/{0}".format(name))

    for resource_name in humbackfile["download"]:

        file_res = get("{0}/{1}".format(humbackfile["url"], resource_name))

        try:
            file_res.raise_for_status()
        except Exception as exc:
            print("ERROR: {0} file downloading error: {1}".format(resource_name, exc))

        if "/" in resource_name:
            files_tree = resource_name.split("/")
            for i in range(0, len(files_tree)-1):
                if i == len(files_tree)-1:
                    with open("apps/{0}/{1}".format(name, files_tree[i]), "wb") as f:
                        for chunk in file_res.iter_content():
                            f.write(chunk)
                        f.close()
                else:
                    mkdir(files_tree[i])
        else:
            with open("apps/{0}/{1}".format(name, resource_name), "wb") as f:
                for chunk in file_res.iter_content():
                    f.write(chunk)
                f.close()

    return True
