import unittest

from htmlnode import LeafNode,ParentNode

class Test_ParentNode(unittest.TestCase):
	def test_with_no_tag_raises_error(self):
		#Should raise an error (no tag)
		#Given no tag when constructing parent node then raise error
		with self.assertRaises(ValueError):
			ParentNode(None,LeafNode("p","Just a paragraph"))

	def test_with_no_children_raises_error(self):
		#Should raise an error (no children)
		with self.assertRaises(ValueError):
			ParentNode("p",None)

	def test_with_one_children_without_props(self):
		#Should have tag and one child
		node = ParentNode("h1",LeafNode("p","This is a paragraph"))
		self.assertEqual(node.to_html(),"<h1><p>This is a paragraph</p></h1>")

	def test_with_one_children_with_props(self):
		#Should have tag with props and one child 
		node = ParentNode("p",LeafNode("a","This is a topic with props", props={"href": "https://www.google.com"}))
		self.assertEqual(node.to_html(),'<p><a href="https://www.google.com">This is a topic with props</a></p>')

	def test_with_multiple_children(self):
		node = ParentNode(
			"p",
			[
			LeafNode("b", "Bold text"),
			LeafNode(None, "Normal text"),
			LeafNode("i", "italic text"),
			LeafNode(None, "Normal text"),
			],)
		self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")



if __name__ == '__main__':
	unittest.main()
