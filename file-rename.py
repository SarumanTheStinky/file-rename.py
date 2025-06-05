import os
import re

renamefolderpath = os.path.dirname(__file__)
oldString = r"oldstring"  
newString = "newstring"

# List all files in the directory
files = [file for file in os.listdir(renamefolderpath)]

for file in files:
    try:
        # Use re.sub() to replace the regex pattern in the filename
        new_file_name = re.sub(oldString, newString, file)
        
        # Rename the file only if the name changes
        if new_file_name != file:
            os.rename(os.path.join(renamefolderpath, file), os.path.join(renamefolderpath, new_file_name))
    except Exception as e:
        print(f"Error renaming {file}: {e}")
