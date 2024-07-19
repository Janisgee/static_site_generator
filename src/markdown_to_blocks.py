import re

def markdown_to_blocks(markdown_string):
  block_list = markdown_string.split('\n\n')
  
  #Strip any leading or trailing whitespace from each block
  #Filter out any empty strings
  final_list = [sentence.strip() for sentence in block_list if sentence.strip() != ""]

  return final_list 


def block_to_block_type(single_block):

  lines = single_block.split('\n')


  if re.match(r'#{1,6} ',single_block):
    return "heading"
  elif single_block.startswith('```') and single_block.endswith('```'):
    return "code"
  elif all(line.startswith('>') for line in lines):
    return "quote"
  elif all(line.startswith('* ') or line.startswith('- ') for line in lines):
    return "unordered_list"
  elif all(re.match(r'^\d+\. ',line) for line in lines):
    for i, line in enumerate(lines):
      if not line.startswith(f'{i+1}. '):
        return "paragraph"
      
    return "ordered_list"
  else:
    return "paragraph"




