import unittest
from textnode import TextNode,text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image
from extraction import split_nodes_image,split_nodes_link

class TestExtraction(unittest.TestCase):

  def test_extract_image_with_plain_text(self):
    node = TextNode(
    "This is just a plain text",
    text_type_text,)

    result = split_nodes_image([node])
    
    self.assertEqual(result,[TextNode("This is just a plain text",
    text_type_text,),])

  def test_extract_image_with_one_image(self):
    node = TextNode(
    "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)",
    text_type_text,)

    result = split_nodes_image([node])
    
    self.assertEqual(result,[TextNode("This is text with a ", text_type_text), TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"),])

  def test_extract_image_with_multiple_image(self):
    node = TextNode(
    "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
    text_type_text,)

    result = split_nodes_image([node])
    
    self.assertEqual(result,[TextNode("This is text with a ", text_type_text), TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"),TextNode(" and ", text_type_text), TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),])

  def test_extract_link_with_one_link(self):
    node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev)",
    text_type_text,)

    result = split_nodes_link([node])
    
    self.assertEqual(result,[TextNode("This is text with a link ", text_type_text), TextNode("to boot dev", text_type_link, "https://www.boot.dev"),])


  def test_extract_link_with_multiple_links(self):
    node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",text_type_text,)

    result = split_nodes_link([node])
    
    self.assertEqual(result,[
    TextNode("This is text with a link ",text_type_text),
    TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
    TextNode(" and ", text_type_text),
    TextNode(
        "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
    ),
])

if __name__ == '__main__':
  unittest.main()

