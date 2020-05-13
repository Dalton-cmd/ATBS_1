import os
for folderName, subfolders, filenames in os.walk(r'c:\users\dalton\desktop\python projects\github\ATBS_1\MiscFiles'):
    print('The folder is ' + folderName)
    print('The subfolder in ' + folderName + ' are: ' +str(subfolders))
    print('The filenames in ' + folderName + ' are: ' +str(filenames))
    print()

    for subfolder in subfolders:
        if 'hello.txt' in subfolder:
            print(subfolder)
            #os.rmdir(subfolder)

    for file in filenames:
        if file.endswith('.py'):
            print(os.join(foldername, file), os.join(folderName, file + '.backup'))
#            shutil.copy(os.join(foldername, file), os.join(folderName, file + '.backup')

os.walk(subfolder,)
