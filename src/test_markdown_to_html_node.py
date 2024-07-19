import unittest
from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLNode

class TestMarkdownToHTMLNode(unittest.TestCase):

  def test_block_type_heading(self):
    markdown ="""
# this is an h1

this is paragraph text

## this is an h2
"""
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    answer ="<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>"
    self.assertEqual(html, answer,)

  def test_block_type_paragraph(self):
    markdown = """
This is **bolded** paragraph
text in a p
tag here

"""
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    answer = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>"
    self.assertEqual(html,answer,)

  def test_block_type_blockquote(self):
    markdown = """
> This is a
> blockquote block

this is paragraph text

"""
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    answer = "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>"
    self.assertEqual(html,answer,)

  def test_block_type_blockquote(self):
    markdown = """
> This is a
> blockquote block

this is paragraph text

"""
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    answer = "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>"

    self.assertEqual(html, answer,)

  def test_block_type_list(self):
    markdown = """

- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""
    node = markdown_to_html_node(markdown)
    html = node.to_html()
   

    answer = "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>"


    self.assertEqual(html, answer,)


  def test_block_type_code(self):
    markdown = """

#### This is a heading

```
        int main(void){
          printf("hello world!")
        }
```

Another paragraph of Cameron
"""
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    answer = """<div><h4>This is a heading</h4><pre><code>
        int main(void){
          printf("hello world!")
        }
</code></pre><p>Another paragraph of Cameron</p></div>"""
    self.assertEqual(html, answer)
  

if __name__ == '__main__':
  unittest.main()