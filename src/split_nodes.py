from textnode import *
from extract_markdown_imglink import *

def create_list(string):
    templist = []
    templist.append(string)
    return templist



def split_nodes_delimiter(old_nodes, delimiter,text_type):

    
    new_nodes = []
    if type(old_nodes) != list:
        old_nodes = create_list(old_nodes)
        


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

def split_nodes_image(old_nodes):

    if type(old_nodes) != list:
        old_nodes = create_list(old_nodes)
    
    new_nodes = []
   
    for node in old_nodes:
        extract = extract_markdown_images(node.text)
        if extract == []:
            return old_nodes             
        
        sections = []
        sections.append(node.text)

        for n in range(len(extract)):
            extractstring = str(extract[n])
            stringlist = extractstring.split(",")
            img_alt = stringlist[0]
            img_alt = img_alt[2:-1]
            image_link = stringlist[1]
            image_link = image_link[2: -2]
            if len(sections) > n:  
                sections = sections[n].split(f"![{img_alt}]({image_link})", 1)
                if len(sections[0]) > 1:
                    new_nodes.append(TextNode(sections[0], "text"))
            new_nodes.append(TextNode(img_alt, "image", image_link))

    print(new_nodes)   
    return(new_nodes)    

def split_nodes_link(old_nodes):

    if type(old_nodes) != list:
        old_nodes = create_list(old_nodes)
    
    new_nodes = []
  
    for node in old_nodes:
        extract = extract_markdown_links(node.text)
        if extract == []:
            return old_nodes             
        
        sections = []
        sections.append(node.text)

        for n in range(len(extract)):
            extractstring = str(extract[n])
            stringlist = extractstring.split(",")
            img_alt = stringlist[0]
            img_alt = img_alt[2:-1]
            image_link = stringlist[1]
            image_link = image_link[2: -2]
            if len(sections) > n:  
                sections = sections[n].split(f"[{img_alt}]({image_link})", 1)
                if len(sections[0]) > 1:
                    new_nodes.append(TextNode(sections[0], "text"))
            new_nodes.append(TextNode(img_alt, "link", image_link))

    print(new_nodes)   
    return(new_nodes)    

#Move this into test file! Write test file! 
split_nodes_image(TextNode(
    " ![to boot dev](https://www.boot.dev) This is text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
    "text",))
split_nodes_link(TextNode(
    "This is text wFUCK YOUimage [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    "text",))