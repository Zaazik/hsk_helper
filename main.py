from untils.dir_helper import find_xmls_by_path, join_path, is_file_exist, convert_and_save
from untils.xml_helper import get_root

HSK_path = """D:\SteamLibrary\steamapps\common\RimWorld\Mods\Core_SK\Defs\\"""
CORE_path = """D:\SteamLibrary\steamapps\common\RimWorld\Mods\Core\Defs\\"""


def start():
    dif = []

    for file_path_without_root in find_xmls_by_path(HSK_path):
        core_file_path = join_path(CORE_path, file_path_without_root)
        hsk_file_path = join_path(HSK_path, file_path_without_root)

        tag_and_name = {}

        if is_file_exist(core_file_path):
            hsk_root = get_root(hsk_file_path)
            core_root = get_root(core_file_path)
            for child in hsk_root:
                tag = child.tag
                defName = child.find("defName")

                if defName ==  None:
                    continue

                tag_and_name[(tag, defName.text)] = True

            for child in core_root:
                tag = child.tag
                defName = child.find("defName")

                if defName == None:
                    continue

                exist = tag_and_name.get((tag, defName.text), False)
                if exist:
                    data = {
                        "path": file_path_without_root,
                        "tag": tag,
                        "defName": defName.text
                    }
                    dif.append(data)
    return dif

if __name__ == '__main__':
    dif = start()
    convert_and_save(dif, prefix=".json")
    print("TOTAL: %s" % len(dif))

