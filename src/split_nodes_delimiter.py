from textnode import *



def split_nodes_delimiter(old_nodes, delimiter,text_type):

    
    new_nodes = []
    if type(old_nodes) != list:
        templist = []
        templist.append(old_nodes)
        old_nodes = templist
        


    for node in old_nodes:
        if node.text_type == "text" and node.url == None:
            ntext = node.text
            splittest = ntext.split(delimiter)
            for n in range(0, len(splittest)):
                if n == 0 or n % 2 == 0:
                    gennode = TextNode(splittest[n], "text")
                    new_nodes.append(gennode)
                else:
                    gennode = TextNode(splittest[n], text_type)
                    new_nodes.append(gennode)

        else:
            new_nodes.append(node)
    return new_nodes
