import unittest

from htmlnode import HTMLNode

class Test_HTMLNode(unittest.TestCase):
	def test_default_initialization(self):
		node = HTMLNode()
		self.assertIsNone(node.tag)
		self.assertIsNone(node.value)
		self.assertIsNone(node.children)
		self.assertIsNone(node.props)

	def test_partial_init_with_tag_value(self):
		node = HTMLNode(tag="p",value="Hello World")
		self.assertEqual(node.tag,"p")
		self.assertEqual(node.value,"Hello World")
		self.assertIsNone(node.children)
		self.assertIsNone(node.props)

	def test_partial_init_with_children_props(self):
		children_nodes = [
				HTMLNode(tag='p', value='First paragraph.'),
				HTMLNode(tag='p', value='Second paragraph.')
				]
		props_dict = {
			"href": "https://www.google.com",
			"target": "_blank"
			}
		node = HTMLNode(children=children_nodes, props= props_dict)
		self.assertIsNone(node.tag)
		self.assertIsNone(node.value)
		self.assertEqual(node.children,children_nodes)
		self.assertEqual(node.props,props_dict)


	def test_props_to_html_no_props(self):
		node=HTMLNode(tag='a')
		self.assertEqual(node.props_to_html(),'')

	def test_props_to_html_single_prop(self):
		node = HTMLNode(tag='a', props={"href": "https://www.google.com"})
		self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

	def test_props_to_html_multiple_props(self):
		node = HTMLNode(tag='img', props={"src":"image.png","alt":"An image"})
		self.assertEqual(node.props_to_html(), ' src="image.png" alt="An image"')




if __name__ == "__main__":
	unittest.main()
