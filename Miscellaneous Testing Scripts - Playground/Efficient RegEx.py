import re

message = 'Call me at 555-555-5555 tomorrow or at 555-555-5555'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')                           #Sets the object (the pattern you want to find) (/d is for digit)
mo = phoneNumRegex.search(message)                                              #mo = Match Object -> creates a match object
print(mo.group())                                                               #group() returns the "matched" strings

## For another view, this functionis performing the same operation
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call me at 555-555-5555 tomorrow or at 555-555-5555')#mo = Match Object
print(mo.group())                                                               #Believe we need to use the mo."group()" in our function in order to read the data correctly

print(phoneNumRegex.findall(message))                                           #Will find all instances and print it as a list



####Notes on RegEx:
## Regular expressions are mini-language for specifying text patterns. Writing
#       code to do pattern matching without using RegEx is a huge operation
## Regex strings often use \backslashes (like \d), so they are often
#       raw strings: r'\d'

###Steps for using the Re module
# Import the re module first
# Call the re.compile() function to create a RegEx object (Your pattern you want to set)
# Call the regex objects "search()" method to create a match object
# Call the match object's group() method to get the matched strings
# \d is the regex for a numeric digit character
