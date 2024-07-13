from textnode import *
from htmlnode import *

def run_test(nname, text, text_type, url, ):
    nname = TextNode(text,text_type,url)
    testnode = text_node_to_html_node(nname)

    print(testnode.to_html())

    

def main():#to rewrite
    testcases = [["test1", "testtext1", "text_type_bold", ""],
                 ["test2", "thisisalink", "text_type_link", "www.google.com"],
                 ["test3", "thisisanimage", "text_type_image", "www.google.com"],
                 ["test4", "this is raw text", "text_type_text", ""],
                 ["test5", "this is italic", "text_type_italic", ""]
        
    ]

    for case in testcases:
            run_test(case[0], case[1], case[2], case[3])


main()