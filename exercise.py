#exercise methods for str

text = " I Love YURI "

def slice():
    a = "I love yuri"
    print(a[7:])

def lower():
    print(text.lower()) #this method will convert the string to all lowercase letters

def upper():
    print(text.upper()) #this method will convert the string to all uppercase letters

def title():
    print(text.title()) #this method will convert the first letter of each word to uppercase and the rest to lowercase

def capitalize():
    print(text.capitalize()) #this method will convert the first letter of the string to uppercase and the rest to lowercase

def swapcase():
    print(text.swapcase()) #this method will convert all uppercase letters to lowercase and all lowercase letters to uppercase

def count():
    print(text.count("YURI")) #this method will count the number of times the specified value appears in the string

def strip():
    print(text.strip()) #this method will remove any whitespace from the beginning and end of the string

def replace():
    print(text.replace("YURI", "Yuri")) #this method will replace the specified value with another value in the string

lower()
upper()
replace()
strip()
slice()
count()
swapcase()
capitalize()
title()