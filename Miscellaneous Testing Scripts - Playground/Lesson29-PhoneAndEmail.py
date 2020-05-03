#! python3
import re, pyperclip

#Todo:
#   1. Create a regex for phone numbers
#   2. Create a regex for email addresses
#   3. Get the text off the clipboard
#   4. Extract the email/phone from this text
#   5. Copy the extracted email/phone to the clipboard

#1: Phone Number RegEx
phoneRegex = re.compile(r'''
# write compile to capture the following options:
# 415-555-0000, 555-5555, (415) 555-5555, 555-0000 ext 12345, ext., x12345

(
((\d\d\d) | (\(\d\d\d\)))?            # area code (is optional: indicated with ?)
(\s|-)?                            # first separator
\d\d\d                             # first 3 digts
(\s|-)?                            # second separator
\d\d\d\d                           # last 4 digits
(((ext(\.)?\s) |x)                  # extension (number part)
(\d{2,5}))?
)                      # extension (number part)

''', re.VERBOSE)

#2: Email address RegEx
emailRegex = re.compile(r'''
(
[a-zA-Z0-9,.+]+            # name part
@                          # at symbol
[a-zA-Z0-9,.+]+            # domain name part
)
''', re.VERBOSE)

#3: Text from clipboard
text = pyperclip.paste()

#4: Extract email/phone from this text
extractedPhone = phoneRegex.findall(text)   #futher work below
extractedEmail = emailRegex.findall(text)   #finished
extractedEmail = ['{} '.format(elem) for elem in extractedEmail]                ## adds an additional space between email and phone for readability

allPhoneNumbers = []                        #further analyzed                   # creates the phonenumber list via appropriate grouping
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#print(extractedEmail)
#print(allPhoneNumbers)

#Function will print the lists stacked on top of each other. Not very helpful in general
#results = '\n'.join(allPhoneNumbers) + '\n' + '\noin(extractedEmail)
#pyperclip.copy(results)

#Function pulls together both lists so that it is User1:Email1 ; User2:Email2
merged_lists = [i + j for i, j in zip(extractedEmail, allPhoneNumbers)]
pyperclip.copy(merged_lists)
print(merged_lists)
