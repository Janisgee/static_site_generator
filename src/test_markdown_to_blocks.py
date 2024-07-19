import unittest
from markdown_to_blocks import markdown_to_blocks,block_to_block_type

class TestMarkdownToBlock (unittest.TestCase):
  def test_markdown_to_block_with_string(self):
    string = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

    result = markdown_to_blocks(string)

    self.assertEqual(result,["# This is a heading","This is a paragraph of text. It has some **bold** and *italic* words inside of it.","* This is the first list item in a list block\n* This is a list item\n* This is another list item"])


class TestBlockToBlockType(unittest.TestCase):
  def test_heading_block(self):
    block = "##### This is a heading."
    result = block_to_block_type(block)
    self.assertEqual(result, "heading")

  def test_code_block(self):
    block = "```This is a code block```"
    result = block_to_block_type(block)
    self.assertEqual(result, "code")

  def test_quote_block(self):
    block = ">This is a quote block 1\n>This is a quote block 2\n>This is a quote block 3"
    result = block_to_block_type(block)
    self.assertEqual(result, "quote")

  def test_unordered_list(self):
    block = "* This is a list\n* This is an other list\n* This is also a list"
    result = block_to_block_type(block)
    self.assertEqual(result, "unordered_list")

  def test_ordered_list(self):
    block = "1. This is a list\n2. This is an other list\n3. This is also a list"
    result = block_to_block_type(block)
    self.assertEqual(result, "ordered_list")




if __name__ == '__main__':
  unittest.main()
