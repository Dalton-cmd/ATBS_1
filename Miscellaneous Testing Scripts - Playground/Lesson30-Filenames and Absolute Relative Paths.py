cwd = 'C:\\Users\\Dalton\\Desktop\\Python Projects\\github\\ATBS_1\\Miscellaneous Testing Scripts - Playground'

#In order to print out a "\" for use in a file path, you need to use two \\
     ##print("\\") #prints one
     ##print('C:\\spam\\eggs.png')

# Or, you can use a raw string
     ##print(r'C:\spam\eggs.png')

import os
os.path.join('folder1', 'folder2', 'folder3', 'file.png')
     ##print(os.sep + "os.sep prints a '\\'") ####Will print out a separator

#pulls down the current working directory
file_Path = os.getcwd()  # os.getcwd() will print out the CURRENT directory

#Changes the Current Working Directory to the string you specify. the C drive
file_Path = os.chdir('c:\\')
     ##print(file_Path)

#Prints the new file_Path, which we just set as "c:\"
file_Path = os.getcwd()   #cwd, or current working directory is the folder that you are in right now
     ##print(file_Path)

###  Relative File Path: ..\, .\, .\fizz, .\fizz\spam.txt
## When using a relative path, if you need to get to another directory at the same level,
#  using the ".." at the beginning of the file path will pull you into that
## Absolute File Paths: C:\, C:\bacon, C:\bacon\fizz

#Setting the current directory back to our script's location in the directory
os.chdir(cwd)

## Using the absolute file path function (abspath) to use the current directory
# and retrieve the path of a file in the same directory your os module is in

#Note: this will result in a file path regardless of whether or not the file exists there or not
path = os.path.abspath('OIP.jpeg')
     ##print(path)

#We can use the abspath to navigate back ".." from the relative position of our cwd as well
path = os.path.abspath('..\\..\\spam.png')
     ##print(path)

#the isabs path will return a boolean value depending on if the referenced path exits or not
path = os.path.isabs('..\\..\\spam.png')
     ##print(path) #returns False as the specified path doesn't exist

path = os.path.isabs(cwd)
     ##print(path) #returns True as our cwd variable is a valid file path

#Using "folder" as an input to our os functions will allow a blanket statement.
path = os.path.isabs('c:\\folder\\folder\\folder')
     ##print(path)

#Using "relpath" we can obtain the relative filepath subsequent to the root you specify (the second variable)
path = os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1')
     ##print(path)

#From the above relpath function, if you want to pull out a certain chunk, use the following:
#dirname: will return the folders that lead to the last folder/file
path = os.path.dirname('c:\\folder1\\folder2\\spam.png')
     ##print(path)  #Prints out c:\folder1\folder2

#basename: will return the last folder/file after the last set of "\\"
path = os.path.basename('c:\\folder1\\folder2\\spam.png')
     ##print(path) #prints out spam.png

#the os.path.exists function will search the file path provided and return a boolean value if it exists or not
path = os.path.exists('c:\\folder1\\folder2\\spam.png')
     ##print(path) #returns False, as the path above does not exists

#validating the current working directory "cwd"
path = os.path.exists(cwd)
     ##print(path) #returns True, as the path provided exists (is our cwd)

#Another example of validating a file path for a different directory
path = os.path.exists('c:\\windows\\system32\\calc.exe')
     ##print(path)

### The following functions will check if the referenced path is a file or a folder
path = os.path.isfile('c:\\folder1\\folder2\\spam.png')
     ##print(path)
     ##print('Row 82')

path = os.path.isdir('c:\\folder1\\folder2\\spam.png')
     ##print(path)
     ##print("Row 85")

# The following .getsize fuction will return the file size
path = os.path.getsize('c:\\windows\\system32\\calc.exe')
     ##print(path) #value in bits

#The following os.listdir function will return a list of all folders/files inside the specified directory
liststring = os.listdir('c:\\windows\\system32')
print(liststring)

#Following function will find the total size of a directory:
totalSize = 0
for filename in os.listdir('c:\\windows\\system32'):
    if not os.path.isfile(os.path.join('c:\\windows\\system32', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('c:\\windows\\system32', filename))

print(totalSize)

#How to make a new directory:
os.makedirs(cwd + '\\test1\\test2') #returns by adding 2 directories into our cwd



### Recap:
# Files have a nmae and a path
# The root folder is the lowest folder. It's C:\ on windows
# In a file path, the folders and filename are separated by backslashes on Windows: "\"
#   and forward slashes "/" on Mac/Linux
# Use the os.path.join() function to combine folders with the correct slash
# The current working direcotry is the folder that any relative paths are "relative" to
# os.getcwd() will return the current working directory
# os.chdir() will change the cwd
# Absoluate paths begin with the root folder, relative paths do not.
# The .folder represents "this folder", the .. folder represents the "parent folder"

#Functions:
# os.path.abspath(): returns an absolute path from the path passed to it
# os.path.isabs(): returns a boolean if the path passed to it is absolute
# os.path.relpath(): returns the relative path between two paths passed to it
# os.makedirs(): can make folders
# os.path.getsize() returns a file's size
# os.listdir() returns a list of strings of filenames
# os.path.exists() returns True if the filename passed to it exists
# os.path.isfile() and os.path.isdir() return True if they were passed a filname or file path
