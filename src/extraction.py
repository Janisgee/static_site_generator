import re
from textnode import TextNode
from extract_markdown import extract_markdown_images,extract_markdown_links

def split_nodes(old_nodes,extract_function,type):
  new_list = []

  #Loop old_nodes list
  for node in old_nodes:
    #Handle empty node image
    if node.text_type != "text":
      new_list.append(node)
      continue

    #Extract item markdown
    items = extract_function(node.text)

    if not items:
      new_list.append(node)
      continue
    
    remaining_text = node.text

    for alt, link in items:
      delimiter = ''
      if type == "image":
        delimiter = f"![{alt}]({link})"
      else:
        delimiter = f"[{alt}]({link})"
      sections = remaining_text.split(delimiter,1)

      if sections[0]:
        new_list.append(TextNode(sections[0],"text"))

      new_list.append(TextNode(f"{alt}",type,f"{link}"))

      remaining_text = sections[1] if len(sections) > 1 else ""
    
    if remaining_text:
            new_list.append(TextNode(remaining_text, "text"))
  
  return new_list

    
def split_nodes_image(old_nodes):
  return split_nodes(old_nodes,extract_markdown_images,"image")

def split_nodes_link(old_nodes):
  return split_nodes(old_nodes,extract_markdown_links,"link")
    
#text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

#return a turple # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

#text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
#return a turple # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]