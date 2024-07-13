from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

def run_test(nname, tag, value, children, props):
    nname = ParentNode(tag,value,children,props)
    nname.__repr__()
    print(nname.to_html())
    

def main():#to rewrite
    testcasesp = [
        ["test1", "p", "", [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],""],
        #["test2", None,"", LeafNode("b", "Bold text"), ""], correctly calls error PN needs a tag
        #["test2", "p","", None, ""]
        ["test1", "p", "", [ParentNode("p", "", [LeafNode("b", "Bold text")],"")],""]
    ]

    for case in testcasesp:
            run_test(case[0], case[1], case[2], case[3], case[4])


main()
