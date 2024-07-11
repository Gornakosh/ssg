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
        print(self.tag, self.value, self.children, self.props)
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, children, props):
        super().__init__(tag, value, children, props)
        self.children = None
        if self.value == None:
            raise ValueError("No Value set")
        
    def to_html(self):
        self_closing_tags = ["img", "input", "br", "hr", "meta", "link"] #what all this does ist the following: it builds the html code by opening with the tag then checking if it's selfclossing then finishing it and returning it depending on what it is. 
        
        if self.value == None:
            raise ValueError("No Value set")
        if self.tag == None or self.tag == "":
            return self.value
        
        outputstring = f"<{self.tag} "
        if self.props != None:
            for attr, value in self.props.items():
                outputstring += f' {attr}="{value}"'
                
        if self.tag in self_closing_tags:
            outputstring += f">"
            return outputstring
        else:
            outputstring += f" {self.value}</{self.tag}>"
        
        return outputstring
        

        
        


