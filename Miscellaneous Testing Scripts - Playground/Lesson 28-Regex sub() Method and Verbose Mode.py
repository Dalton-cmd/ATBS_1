#The sub() regex method will substitute matches with some other text.
#Using \1, \2 and so will substitute group 1, 2, etc in the regex pattern.
#Passing re.VERBOSE lets you add whitespace and comments to the regex string passed to re.compile().
#If you want to pass multiple arguments (re.DOTALL , re.IGNORECASE, re.VERBOSE), combine them with the | bitwise operator.


###### Course Content #######
import re
namesRegex = re.compile(r'Agent \w+')                                           #Finds instances of Agent "\w" for any word input
mo = namesRegex.findall('Agent Alice gave the documents to Agent Bob')
print(mo)

#to substitute data (or redact names in this example), use the .sub function
mo = namesRegex.sub('REDACTED', 'Agent Alice gave the documents to Agent Bob')
print(mo)                                                                       #When you print using the .sub() function, it will print the entire string with the subs


##Find and Replace function via a Regular Expression
namesRegex = re.compile(r'Agent (\w)\w*')                                       #One specific group, and then one more more* word characters
mo = namesRegex.findall('Agent Alice gave the documents to Agent Bob')          # Results in "A" and "B", which are group 1: Agent "A" and group 2: Agent "B". The "group" is A or B
print(mo)

mo = namesRegex.sub(r'Agent \1---', 'Agent Alice gave the documents to Agent Bob')
print(mo)


#Verbose function for re.compile. Use with triple quote ''' and allows you to make commented code with line breaks
re.compile(r'''
\d\d\d          # area code
-               # first dash
\d\d\d          # first 3 digits
-               # second dash
\d\d\d\d        # last 4 digits
''', re.IGNORECASE | re.DOTALL | re.VERBOSE)                                    #bitwise operator "|" is used (only) within the RegEx function to use multiple options
