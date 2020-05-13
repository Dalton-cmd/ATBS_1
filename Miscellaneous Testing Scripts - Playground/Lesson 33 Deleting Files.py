import os
print(os.getcwd())

# os.rmdir will delete a directory
#os.rmdir(r'c:\fakeDirectory\notRealDirectory')

## this will also let you delete/augment a Directory
import shutil
#shutil.rmtree(r'c:\delicious')

import os

os.chdir(r'c:\users\dalton\desktop')

for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)

import send2trash
send2trash.send2trash(r'c:\users\dalton\desktop\test.txt')

# Function summary:
# os.unlink() will delete a file
# os.rmdir() will delete a folder (but the folder must be empty)
# shutil.rmtree() will delete a folder and all its contents
#### Note!!! Delete files can be dangerous, so do a dry run by printing the file name first
# If you delete using these above functions, it will permannently delete

# send2trash.send2trash() will send a file or folder to the recycling bin
