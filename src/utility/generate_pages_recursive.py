import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

  dir_list = os.listdir(dir_path_content)

  for item in dir_list:
    # Check files or directory in list
    item_path = os.path.join(dir_path_content,item)
    isFile = os.path.isfile(item_path)
    # Set file name
    name = item.split('.')
    file_name = f'{name[0]}.html'
    # if it is File
    if isFile:
      generate_page(item_path, template_path, dest_dir_path,file_name)
    else:
    # if it is directory
      #create same directory in dest
      new_dir_des = os.path.join(dest_dir_path,item)
      os.mkdir(new_dir_des)
      generate_pages_recursive(item_path, template_path, new_dir_des)

  

