import re
from markdown_to_blocks import markdown_to_blocks,block_to_block_type
from text_to_textnodes import text_to_textnodes
from converters import text_node_to_html_node


from htmlnode import ParentNode, LeafNode


def text_to_children(text):
  htmlNode_list = []
  textnodes = text_to_textnodes(text)
  for textnode in textnodes:
    leafNode = text_node_to_html_node(textnode)
    htmlNode_list.append(leafNode)

  return htmlNode_list



def markdown_to_html_node(markdown):
  htmlnode_list=[]
  #1.Split the markdown into blocks
  blocks = markdown_to_blocks(markdown)

  #2.Loop over each block
  for block in blocks:
    #2.1 Determine the type of block 
    block_type = block_to_block_type(block)
    #2.2 Based on the type of block, create a new HTMLNode with the proper data
    
    if block_type == "heading":
      h_num=0
      text_list = block.split()
      for text in text_list:
        if '#' in text:  
            h_num=len(text)
      h_text = ' '.join(text_list[1:])
      children = text_to_children(h_text)
      htmlnode = ParentNode(f'h{h_num}',children)
      htmlnode_list.append(htmlnode)

    elif block_type == "paragraph":
      sentence_list = block.split('\n')
      paragraph = " ".join(sentence_list)
      children = text_to_children(paragraph)
      htmlnode = ParentNode('p',children)
      htmlnode_list.append(htmlnode)

    elif block_type == "quote":
      new_list = []
      value = block.replace('>','')
      sentence_list = value.split('\n')
      for sentence in sentence_list:
        sentence = sentence.strip()
        if sentence == '':
          continue
        new_list.append(sentence)
      new_sentence = " ".join(new_list)
      children = text_to_children(new_sentence)
      htmlnode = ParentNode('blockquote',children)
      htmlnode_list.append(htmlnode)

    elif block_type == "unordered_list":
      #TODO: use text_to_children function from above and do the same as type:quote
      html_list=[]
      new_list=[]
      value=re.sub("- ","",block)
      value=re.sub("^\* ","",value)
      sentence_list = value.split('\n')
      for sentence in sentence_list:
        sentence = sentence.strip()
        if sentence == '':
          continue
        new_list.append(sentence)

      for text in new_list:
        children = text_to_children(text)
        html = ParentNode('li',children)
        html_list.append(html)
      
      htmlnode = ParentNode('ul',html_list)
      htmlnode_list.append(htmlnode)

    elif block_type == "ordered_list":
      html_list=[]
      new_list=[]
       
      sentence_list = block.split('\n')
      for sentence in sentence_list:
        if sentence == '':
          continue
        words = sentence.split()
        new_sentence=' '.join(words[1:])
        new_list.append(new_sentence)

      for text in new_list:
        children = text_to_children(text)
        html = ParentNode('li',children)
        html_list.append(html)
      
      htmlnode = ParentNode('ol',html_list)
      htmlnode_list.append(htmlnode)

    elif block_type == "code":
      value = block.replace('```','')
      children = LeafNode('code', value=value)
      childrenNode = ParentNode('pre', children = children)
      htmlnode_list.append(childrenNode)

  parent_htmlnode = ParentNode('div', children= htmlnode_list)
 
  return parent_htmlnode

# markdown="""This is a paragraph.

# This is another paragraph.
# """
# markdown_to_html_node(markdown)


