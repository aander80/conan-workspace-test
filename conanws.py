import os
name = "myws"

def editables(*args, **kwargs):
    result = {}
    for f in os.listdir(workspace_api.folder):
        if os.path.isdir(f):
            conanfile = workspace_api.load(os.path.join(f, "conanfile.py"))
            result[f"{conanfile.name}/{conanfile.version}"] = {"path": f}
    return result
