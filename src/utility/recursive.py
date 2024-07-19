import os
import shutil

def recursive(source, destination):
    # Step 1: Delete the destination directory if it exists
    if os.path.exists(destination):
        shutil.rmtree(destination)
        
    # Step 2: Create the destination directory fresh
    os.makedirs(destination, exist_ok=True)

    # Step 3: Iterate over all the items in the source directory
    for item in os.listdir(source):
        src_path = os.path.join(source, item)
        dst_path = os.path.join(destination, item)
        
        # If the item is a directory, recursively copy its contents
        if os.path.isdir(src_path):
            recursive(src_path, dst_path)
        else:  # If the item is a file, copy it directly
            shutil.copy(src_path, dst_path)