import re
batRegex = re.compile(r'Bat(wo)?man')                                           #Allows for "wo" to be an input, but does not require it

mo = batRegex.search('The Adventures of Batman')
print(mo.group())                                                               #yields Batman as an output

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())                                                               #yields BatWOman as an output

mo = batRegex.search('The Adventures of Batwowoman')                            #Printing the batRegex.search function yields an error. Storing output in mo via boolean
print(mo)                                                                       #does not yield a result, as we only allow for one "wo"


batRegex = re.compile(r'Bat(wo)*man')                                           #Allows for as many "wo" as we want by using the *
mo = batRegex.search('The Adventures of Batwowowoman')
print(mo.group())

mo = batRegex.search('The Adventures of Batman')
print(mo.group())

VowelRegex = re.compile(r'[aeiouAEIOU]')                                        #findall will search for all instances and return as a list of strings
mo = VowelRegex.findall("pools your eek eat ear")                               #Finds all instances of various vowels in the "[]"
print(mo)

DoubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
mo = DoubleVowelRegex.findall("pools your eek eat ear")                         #Finds all instances of double vowels ( the {2} indicates a search for double in the [textinput])
print(mo)

GreedyRegex = re.compile(r'(ha){3,5}')
mo = GreedyRegex.search("hahahahaHaHaha")
print(mo.group())

testRegex = re.compile(r'(obnoxious)')
mo = testRegex.findall('the motorcyclists are obnoxious all the time')
print(mo)


##notes:
#The regex method findall() is passed a stiring, and returns all matches in it,
#not just the first match.
#if the regex has 0 or 1 group, findall() returns a list of strings
#If the regex has 2 or more groups, finall() returns a list of tuples of strings
# \d is a shorthand character class that matches digits. \w matches word characters,
# \s matches whitespaces characters
# The uppercase shorthand character classed \D, \W, \S match characters that
# are NOT digits, word characters, and spaces
# You can make your own character classes with square brackets: [aeiou]
# A ^ caret makes it a negative character class, matching anything not in the
# bracket [aeiou]
