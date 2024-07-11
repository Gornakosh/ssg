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
    
