##Setting the sample directory for this exercise
exampleDir = 'C:\\Users\\Dalton\\Desktop\\Python Projects\\github\\ATBS_1\\MiscFiles\\hello.txt'

#Sets a variable to open our hello.txt file
helloFile = open(exampleDir)
content = helloFile.read()
print(content)

#Closes the hello.txt file. Running this function susbequent to that above will prevent us from running "content" which calls the read function
helloFile.close()

#Sets the variable to open our hello.txt file in order to readlines, which shows the '\n'
#and prints in a single line string
helloFile = open(exampleDir)
content = helloFile.readlines()
print(content)

#Writes new content to our original file
helloFile = open(exampleDir, 'w')
content = helloFile.write('Hello! We have just re-written to this txt') #write will also return the number of characters you input (the 42 )
print(content)
helloFile.close()

##Creating a new txt file, which posts to our cwd
baconFile = open('bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable')
baconFile.close()

#importing os modules to see the cwd and identify where it wrote the file to
import os
print(os.getcwd())

#Now, let's append instead of re-writing the data
baconFile = open('bacon.txt', 'a')
baconFile.write('\n\n Bacon is delicious.')
baconFile.close()

import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
shelfFile['cats']
list(shelfFile.keys())
list(shelfFile.values())

### The shelve module can store Python values in a binary file
#   shelve.open() returns a dictionary-like shelf value
