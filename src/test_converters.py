import unittest

from  converters import text_node_to_html_node
from textnode import (TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_image, text_type_link,)
from htmlnode import LeafNode

class TestTextNodeToHTMLNode(unittest.TestCase):
	def test_text_node_to_leaf_node_text(self):
		text_node = TextNode("Just plain text", text_type_text)
		leaf_node = text_node_to_html_node(text_node)
		expected_node = LeafNode(tag=None, value= "Just plain text")

		self.assertEqual(leaf_node, expected_node)

	def test_text_node_to_leaf_node_bold(self):
		text_node = TextNode("Just bold text", text_type_bold)
		leaf_node = text_node_to_html_node(text_node)
		expected_node = LeafNode(tag="b", value= "Just bold text")

		self.assertEqual(leaf_node, expected_node)

	def test_text_node_to_leaf_node_italic(self):
		text_node = TextNode("Just italic text", text_type_italic)
		leaf_node = text_node_to_html_node(text_node)
		expected_node = LeafNode(tag="i", value= "Just italic text")

		self.assertEqual(leaf_node, expected_node)

	def test_text_node_to_leaf_node_code(self):
		text_node = TextNode("Just code text", text_type_code)
		leaf_node = text_node_to_html_node(text_node)
		expected_node = LeafNode(tag="code", value= "Just code text")

		self.assertEqual(leaf_node, expected_node)

	def test_text_node_to_leaf_node_image(self):
		text_node = TextNode("Just an image", text_type_image,"https://www.boot.dev")
		leaf_node = text_node_to_html_node(text_node)
		expected_node = LeafNode(tag="img", value= "", props = {"src":text_node.url, "alt":text_node.text})

		self.assertEqual(leaf_node, expected_node)

	def test_text_node_to_leaf_node_link(self):
		text_node = TextNode("Just a link", text_type_link,"https://www.boot.dev")
		leaf_node = text_node_to_html_node(text_node)
		expected_node = LeafNode(tag = "a", value= text_node.text, props = {"href":text_node.url})

		self.assertEqual(leaf_node, expected_node)





if __name__ == '__main__':
	unittest.main()
