import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        #node3 = TextNode("this is a text", "XXXX", "LOL")
        #node4 = TextNode("no","no")
        #self.assertEqual(node3,node4)
        node5 = TextNode("this is a text", "XXXX", None)
        node6 = TextNode("this is a text", "XXXX", None)
        self.assertEqual(node5,node6)

if __name__ == "__main__":
    unittest.main()
