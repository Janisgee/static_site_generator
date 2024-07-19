import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image

class TextSplitNodesDelimiter(unittest.TestCase):
	def test_bold_case(self):
		node = TextNode("This is text with a **bold phrase** inside", "text")
		result = split_nodes_delimiter([node], "**", "bold")

		self.assertEqual(len(result),3)

		self.assertEqual(result[0].text,"This is text with a ")
		self.assertEqual(result[0].text_type, "text")

		self.assertEqual(result[1].text,"bold phrase")
		self.assertEqual(result[1].text_type, "bold")

		self.assertEqual(result[2].text," inside")
		self.assertEqual(result[2].text_type,"text")

	def test_italic_case(self):
		node = TextNode("This is text with a *italic phrase* inside", "text")
		result = split_nodes_delimiter([node], "*", "italic")

		self.assertEqual(len(result),3)

		self.assertEqual(result[0].text,"This is text with a ")
		self.assertEqual(result[0].text_type, "text")

		self.assertEqual(result[1].text,"italic phrase")
		self.assertEqual(result[1].text_type, "italic")

		self.assertEqual(result[2].text," inside")
		self.assertEqual(result[2].text_type,"text")

	def test_code_case(self):
		node = TextNode("This is text with a `code phrase` inside", "text")
		result = split_nodes_delimiter([node], "`", "code")

		self.assertEqual(len(result),3)

		self.assertEqual(result[0].text,"This is text with a ")
		self.assertEqual(result[0].text_type, "text")

		self.assertEqual(result[1].text,"code phrase")
		self.assertEqual(result[1].text_type, "code")

		self.assertEqual(result[2].text," inside")
		self.assertEqual(result[2].text_type,"text")

	def test_no_delimiters(self):
		node = TextNode("This is a plain text with no delimiters", "text")
		result = split_nodes_delimiter([node], "**", "bold")

		self.assertEqual(len(result),1)
		self.assertEqual(result[0].text,"This is a plain text with no delimiters")
		self.assertEqual(result[0].text_type,"text")




if __name__ == '__main__':
	unittest.main()
