#basic RegEx function to find a phone number
#highly inefficient and does NOT utilize the RegEx functionality
def isPhoneNumber(text):
    if len(text) != 12:                                                         #Checks that the input is at least 12 characters long
        return False
    for i in range(0, 3):                                                       #$Checks that there is an area code
        if not text[i].isdecimal():
            return False
    if text[3] != '-':                                                          #Checks that there are dashes
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False                                                        #No first 3 digits
    for i in range(8,12):
        if not text[i].isdecimal():
            return False                                                        #Missing the last 4 digits
    return True

message = 'Call me at 555-555-4555 tomorrow, or at 444-444-4544. thanks'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('phone number found ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers')
