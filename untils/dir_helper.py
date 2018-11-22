import os

def find_xmls_by_path(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.xml'):
                yield ("%s\\%s"%(root, file)).replace(path,"")

def join_path(path_f, path_s):
    return path_f+path_s

def is_file_exist(file_path):
    return os.path.exists(file_path)

def convert_and_save(data, prefix=".text"):
    import json
    with open('data'+prefix, 'w') as outfile:
        if prefix == ".json":
            json.dump(data, outfile)
        else:
            str = ""
            for i in data:
                for k in i:
                    str += k + ": " + i[k] + "\n"

                str += "\n"

            outfile.write(str)
