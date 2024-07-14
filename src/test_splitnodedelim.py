from split_nodes_delimiter import *



def test():
    testcases = [["`", "code", TextNode("This is text with a `code block` word", "text",)],
                 ["**", "bold", [TextNode("This is text with a **bold** word", "text",), TextNode("This is a textnode with an *italic* word", "text")]],
                 ["*", "italic", [TextNode("This is a textnode with an *italic* word", "text"),TextNode("This is a textnode with a 2nd *italic* word", "text")]]
                ]
    for case in testcases:
        print(split_nodes_delimiter(case[2], case[0], case[1]))




def main():
    test()

main()