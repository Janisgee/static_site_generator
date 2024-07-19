from textnode import TextNode, text_type_text, text_type_bold,text_type_italic, text_type_code, text_type_link, text_type_image
from split_nodes_delimiter import split_nodes_delimiter
from extraction import split_nodes_image, split_nodes_link



def text_to_textnodes(text):

  nodes = [TextNode(text, text_type_text)]
  nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
  nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
  nodes = split_nodes_delimiter(nodes, "`", text_type_code)
  nodes = split_nodes_image(nodes)
  nodes = split_nodes_link(nodes)
 
  return nodes
    


# text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)")


# [
#     TextNode("This is text with a ", "text"),
#     TextNode("bolded phrase", "bold"),
#     TextNode(" in the middle", "text"),
# ]


# text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)")