


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented  
    
    def props_to_html(self):
        output = ""
        if self.props == None:
            return "no props set"
        for key, value in self.props.items():
            output +=  f' {key}="{value}"'
        return output
                
    def __repr__(self):
        return f"Main(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, children, props)
        self.children = None
        if self.value == None:
            raise ValueError("No Value set")
        
    def to_html(self):
        self_closing_tags = ["img", "input", "br", "hr", "meta", "link"] #what all this does ist the following: it builds the html code by opening with the tag then checking if it's selfclossing then finishing it and returning it depending on what it is. 
        
        if not self_closing_tags and self.value == None :
            raise ValueError("No Value set") 
        if self.tag in self_closing_tags:
            # Handle self-closing tags
            outputstring = f"<{self.tag}"

            # Add any properties
            if self.props:
                for attr, value in self.props.items():
                    outputstring += f' {attr}="{value}"'

            outputstring += " />"  # Close the self-closing tag
            return outputstring

        else:
            # Handle normal tags that enclose content
            if not self.tag:
                # No tag, just return the value
                return self.value

            outputstring = f"<{self.tag}"

            # Add any properties
            if self.props:
                for attr, value in self.props.items():
                    outputstring += f' {attr}="{value}"'

            outputstring += ">"  # Close the opening tag
            
            if self.value:
                outputstring += self.value

            outputstring += f"</{self.tag}>"  # Add the closing tag
            return outputstring
    
class ParentNode(HTMLNode):
    def __init__(self, tag, value, children, props):
        super().__init__(tag, value, children, props)
        self.value = None

    def  to_html(self):
        
        if self.tag == None or self.tag == "":
            raise ValueError("ParentNode needs a tag")
        
        if self.children == None or self.children == "":
            raise ValueError("Parent node needs children!")
        childrenlist = self.children.copy()
        #may work...
        def html_string(childrenlist):
            tagind = len(self.tag) + 2
            if len(childrenlist) == 0:
                htmlstring = f"<{self.tag}></{self.tag}>"
                return htmlstring
            else:
                htmlstring = html_string(childrenlist[1:])
                #construct the children string: 
                htmlstring = htmlstring[:tagind] + childrenlist[0].to_html() + htmlstring[tagind:]
            return htmlstring
        
        return html_string(childrenlist)

def text_node_to_html_node(text_node):
    if text_node.text_type not in ["text_type_text", "text_type_bold", "text_type_italic", "text_type_code", "text_type_link", "text_type_image"]:
       raise ValueError("Unsupported text type")

    if text_node.text_type == "text_type_text":
        return LeafNode(tag="", value=text_node.text)
    elif text_node.text_type == "text_type_bold":
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == "text_type_italic":
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == "text_type_code":
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == "text_type_link":
        props = {"href": text_node.url}
        return LeafNode(tag="a", value=text_node.text, props=props)
    elif text_node.text_type == "text_type_image":
        props = {"src": text_node.url, "alt": text_node.text}
        return LeafNode(tag="img", value="", props=props)
    
    
     




        
        


