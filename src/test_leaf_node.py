import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

	def test_leaf_without_tag(self):
		node = LeafNode(None,"Just some text")
		self.assertEqual(node.to_html(),"Just some text")

	def test_leaf_with_tag_no_props(self):
		node = LeafNode("p","This is a paragraph.")
		self.assertEqual(node.to_html(),"<p>This is a paragraph.</p>")

	def test_leaf_with_tag_and_props(self):
		node = LeafNode("a","Click here",{"href":"http://www.example.com"})
		self.assertEqual(node.to_html(),'<a href="http://www.example.com">Click here</a>')

	def test_leaf_no_value_raises_error(self):
		with self.assertRaises(ValueError):
			LeafNode("p",None)


if __name__ == '__main__':
	unittest.main()
