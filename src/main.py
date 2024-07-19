import sys
from textnode import TextNode
sys.path.insert(0,'/mnt/c/Users/janis/python_projects/static_sites/src/utility')
from recursive import recursive
from generate_pages_recursive import generate_pages_recursive


def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)
    
    # Move files between directories
    source_dir = '/mnt/c/Users/janis/python_projects/static_sites/static'
    destination_dir = '/mnt/c/Users/janis/python_projects/static_sites/public'
    recursive(source_dir, destination_dir)

    # Generate page recursive from markdown to html
    from_path = "/mnt/c/Users/janis/python_projects/static_sites/content"
    template_path = "/mnt/c/Users/janis/python_projects/static_sites/template.html"
    dest_path = "/mnt/c/Users/janis/python_projects/static_sites/public"
    generate_pages_recursive(from_path,template_path,dest_path)



main()
