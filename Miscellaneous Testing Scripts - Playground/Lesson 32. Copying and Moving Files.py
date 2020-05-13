import os
import shutil

#shutil.copy will copy a specific file from the (source, destination)
shutil.copy(r'C:\Users\Dalton\Desktop\Python Projects\github\ATBS_1\MiscFiles\hello.txt', r'c:\Users\Dalton\Desktop\Python Projects\github\ATBS_1')

#shutil.copy can also be used to copy a file to a new location, with a new name (just add the same extension to indicate end of tree root)
shutil.copy(r'C:\Users\Dalton\Desktop\Python Projects\github\ATBS_1\MiscFiles\hello.txt', r'c:\Users\Dalton\Desktop\Python Projects\github\ATBS_1\MiscFiles\HelloHello.txt')

#shutil.copytree will copy an entire folder's contents
##shutil.copytree(r'C:\users\dalton\desktop\python projects\github\ATBS_1\MiscFiles', r'c:\users\dalton\desktop\Python Projects\github\ATBS_1\MiscFilesBackup')

#shutil.move will move a file to a new location and rename it. Here we just move it to the same folder with a new name
shutil.move(r'C:\users\dalton\desktop\python projects\github\ATBS_1\MiscFilesBackup\pylogo.jpg', r'c:\users\dalton\desktop\Python Projects\github\ATBS_1\MiscFilesBackup\pythonlogo.jpg')
