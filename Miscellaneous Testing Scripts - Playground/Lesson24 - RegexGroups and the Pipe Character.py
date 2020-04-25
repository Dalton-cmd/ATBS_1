import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.search('My number is 555-555-5555')
mo = phoneNumRegex.search('My number is 555-555-5555')
print(mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')                     #parenthesis bifurcate it into different "groups"
mo = phoneNumRegex.search('My number is 555-555-5555')
print(mo.group())                                                               #prints the entire match, and does NOT specify a "group"
print(mo.group(1))                                                              #prints the first "group", which is the area code in this example (group indicated by "()" in our object)
print(mo.group(2,3))                                                            #prints the 2nd and 3rd group

phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is (605) 585-5555')                        #Not sure why, but won't work if there is not a space or '-' between group 1 and 2
print(mo.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('the Batmobile lost a wheel and took the Batcopter')       #will only find the first instance
print(mo.group())                                                               #Returns Batmobile
print(mo.group(1))                                                              #Returns mobile

mo = batRegex.search('Batmotorcycle lost a wheel')
#print(mo.group())                                                              #won't print since Batmotorcycle is not a valid item for our parameters
test = mo == None
print(test)                                                                     #shows that mo == None; prints True




##### Notes over RegEx:
# Groups are created in regex strings with parentheses (see line 7)
# The first set of parentheses is group 1, then group 2, and so on
# Calling group() or group(0) returns the full matching string, while group(1)
# returns group 1's matching string, and so on. So using 1, 2, 3+ gets a more precise response
# Use \(and \) to match literal parentheses in the reges string (e.g, in row 13)
# The | pipe can match one of many possible groups
