import re
beginsWithHelloRegex = re.compile(r'^Hello')                                    # the carot ^ requires the text pattern "Hello" to begin at the beginning of the string
mo = beginsWithHelloRegex.search('Hello there!')
print(mo.group())

mo = beginsWithHelloRegex.search('He said "Hello!"') == None                    #Carot will not pick up our phrase inside quotes
print(mo)

endsWithWorldRegex = re.compile(r'world!$')                                     # the $ requires the text pattern to be at the end of the strings
mo = endsWithWorldRegex.search('Hello world!')
print(mo.group())

mo = endsWithWorldRegex.search('Hello world!slkdfjwoeijfosm')
print(mo)

allDigitsRegex = re.compile(r'^\d+$')                                           #pattern has to be completely: \d, which is just a digit
mo = allDigitsRegex.search('2156481465489')
print(mo.group())

mo = allDigitsRegex.search('516546YYYYYYYY2641') == None                        #pattern cannot submit with a word character within it, as it resultes in a None value
print(mo)


atRegex = re.compile(r'.at')                                                    #using a period "." will pick up ANY character prior to the folowing characters "at"
mo = atRegex.findall('The cat in the hat sat on the flat mat with the rat.')
print(mo)

atRegex = re.compile(r'.{1,2}at')                                               #pickups up 1 to 2 characters before our paramter of "at", which also includes spaces " "
mo = atRegex.findall('The cat in the hat sat on the flat mat with the rat.')
print(mo)

#.* will match anything                                                         #Greedy:      (.*)
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')                     #Non-Greedy:  (.*?)
mo = nameRegex.findall('First Name: John Last Name: Smith')
print(mo)

#Greedy vs Non Greedy Example:
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')                                              #NON Greedy -> looking for anything (.*?) as long as it as the brackets < >, but as little "?" as possible
mo = nongreedy.findall(serve)
print(mo)

greedy = re.compile(r'<(.*)>')
mo = greedy.findall(serve)                                                      #Greedy match: looks for ALL text within brackets. Skips the first bracket, but still fulfils by going to second
print(mo)

prime = 'Serve the public trust. \nProtect the innocent. \nUpload the law.'
print(prime)

dotStar = re.compile(r'.*')
mo = dotStar.search(prime)                                                      #matches everything up to new line, because the "." can be anything except the new line \n
print(mo)

#To get DOT to match any character, use following:
dotStar = re.compile(r'.*', re.DOTALL)
mo = dotStar.search(prime)
print(mo)

vowelRegex = re.compile(r'[aeiou]')
mo = vowelRegex.findall('Al, why does your programming book talk about robocops so much?')
print(mo)

vowelRegex = re.compile(r'[aeiou]', re.I)                                       #re.I will ignore case. Now we (using .findall) will find the "A"
mo = vowelRegex.findall('Al, why does your programming book talk about robocops so much?')
print(mo)

### Summary Notes:
## The ^ means the string must start with the pattern, $ means the string must
#    end with the pattern. both means the ENTIRE string must match the pattern.
## The . dot can be used as a wildcard; it matched anything excep newlines.
## Pass re.DOTALL as the second argument to re.compile() in order to make
#    the . dot match newlines (\n) as well
## Pass re.I as the second argument to re.compile() to make the matching set to
#    Case INSENSITIVE
