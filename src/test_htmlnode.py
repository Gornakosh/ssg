from htmlnode import HTMLNode
from htmlnode import LeafNode


def run_test(nname, tag, value, children, props):
    nname = HTMLNode(tag,value,children,props)
    nname.__repr__()
    print(nname.props_to_html())

def run_test_leaf(nname, tag, value, children, props):
    nname = LeafNode(tag,value,children,props)
    nname.__repr__()
    print(nname.to_html())

    
def main():
    testcases = [
        ["test1", "p", "this is a test text", ["testx", "testy"], {"href": "www.google.com", "hrep": "www.20min.ch"}],
        ["test2", "a", "this is another test", ["xxx", "yyyy"], {"href": "www.9gag.com", "hrep": "www.youtube.com"}],
        ["test3", "", "", [], None],
        ["test4", None, None, None, None]       
    ]
    
    leaftests = [
        ["testl1", "p", "this is a leaftest text", None, None],
        ["testl2", "img", "click this image", None,{"href": "www.google.com",}],
        ["testl3", None, "this should be plain text", "xxx", None]
    ]

    for case in testcases:
        run_test(case[0], case[1], case[2], case[3], case[4])
    #ToDo: Write test cases for LeafNode!
    for case in leaftests:
        run_test_leaf(case[0], case[1], case[2], case[3], case[4])

main()
