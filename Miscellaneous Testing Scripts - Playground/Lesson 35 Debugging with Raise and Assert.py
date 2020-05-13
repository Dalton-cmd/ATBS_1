#Calling the Raise function will spit out the standard error message with your own custom message
#raise Exception('This is an error message')

'''
************
*          *
*          *
*          *
************

'''

import traceback
assert False, 'This is the error message'  #prints an asserted error

### This function will print an error log to a new text file within the cwd
"""
try:
    raise Exception('This is an error message')
except:
    errorFile = open('error_log.txt','a') #runs using append mode
    errorFile.write(traceback.format_exc())
    print('The traceback info was written error_log.txt')

import os
print(os.getcwd()) # file prints to this wd
"""


### Function shows how to raise an exception
'''
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol is 2 characters')
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width-2) )+ symbol)

    print(symbol * width)

boxPrint('*', 15, 5)
boxPrint('O', 5, 16)
'''
