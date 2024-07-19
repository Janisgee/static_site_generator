import re

def extract_title(markdown):
  lines = markdown.split('\n')
  for line in lines:
    is_heading_h1 = re.findall("^# ",line)
    if is_heading_h1:
      h1_words = line.split(' ')
      h1 = " ".join(h1_words[1:])
      return h1
    else:
      raise Exception ('There is no h1 heading')
  
