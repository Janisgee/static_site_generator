import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
  def test_markdown_with_different_block(self):
    markdown ="""

### This is a heading.

This is a sentence

# This is a h1 heading


""" 
    h1_result = extract_title(markdown)
    self.assertEqual(h1_result,"This is a h1 heading")

  def test_markdown_with_h1_only(self):
    markdown ="""

# This is a h1 heading

""" 
    h1_result = extract_title(markdown)
    self.assertEqual(h1_result,"This is a h1 heading")

  def test_markdown_without_h1(self):
    markdown = """"

This is a paragraph1.

This is a paragraph2.

This is a paragraph3.


""" 
    with self.assertRaises(Exception):
      extract_title(markdown)

if __name__ == '__main__':
  unittest.main()