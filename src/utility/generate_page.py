import sys
sys.path.insert(0, '/mnt/c/Users/janis/python_projects/static_sites/')
sys.path.insert(0, '/mnt/c/Users/janis/python_projects/static_sites/src')

from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLNode
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path,new_file_name):
  # Create a message 
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")

  #Read the markdown file - from_path and store the content
  template = open(template_path,"r")
  template_html = template.read()
  #Read the markdown file - template_path and store the content
  md_content = open(from_path,"r")
  content = md_content.read()

  #Convert markdown to html
  node = markdown_to_html_node(content)
  content_html = node.to_html()
  # print(content_html)

  #Capture the title
  h1_heading = extract_title(content)

  #Replace the {{ Title }} and {{ Content }} placeholders in the template
  #Update Title
  update_title_template = template_html.replace("{{ Title }}", h1_heading)
  
  #Update Content
  final_update_template = update_title_template.replace("{{ Content }}", content_html)

  #Write updated template to destination path
  #Create a file in dest
  file_name = f"/{new_file_name}"
  dest_file = open(dest_path+file_name,"w")
  dest_file.write(final_update_template)
  dest_file.close()
  

  











