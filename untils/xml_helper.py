import xml.etree.ElementTree

def print_tree(root, tabs = ""):
    tabs += "\t"
    for child in root:
        str = "%s" % child.tag
        if (child.text != None) and child.text.strip(' \t\n\r') != "" :
            str += ": %s" % (child.text)
        print(tabs,str)
        print_tree(child, tabs=tabs)
    return
# print_tree(root)

def get_root(path):
    return xml.etree.ElementTree.parse(path).getroot()
