import re

def extract_markdown_images(text):
    found = re.findall(r"!\[(.*?)\]\((.*?)\)", text)

    return found

def extract_markdown_links(text):
    found = re.findall(r"\[(.*?)\]\((.*?)\)", text)

    return found




def main():
    print(extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"))
    print(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"))
main()