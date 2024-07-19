from textnode import TextNode, text_type_text, text_type_bold,text_type_italic, text_type_code, text_type_link, text_type_image
from htmlnode import LeafNode

def text_node_to_html_node(text_node):

	if text_node.text_type == text_type_text:
		# Handle converting a plain text TextNode to a LeafNode
		return LeafNode(tag = None, value = text_node.text)

	elif text_node.text_type == text_type_bold:
		return LeafNode(tag = "b", value = text_node.text)

	elif text_node.text_type == text_type_italic:
		return LeafNode(tag = "i", value = text_node.text)

	elif text_node.text_type == text_type_code:
		return LeafNode(tag = "code", value = text_node.text)

	elif text_node.text_type == text_type_link:
		return LeafNode(tag = "a", value= text_node.text, props = {"href":text_node.url})
        
	elif text_node.text_type == text_type_image:
		return LeafNode(tag = "img", value = text_node.text, props = {"src":text_node.url, "alt":text_node.text})
        
	else:
		raise ValueError(f"Unsupported TextNode type: {test_node.text_type}")






	return leaf_node

	
