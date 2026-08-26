
#random variables:
a = "J sucks"
b = "J is amazing"
fact = "facts!"

#more variables:
vegetables = ["carrots", "broccoli", "spinach"] #list of vegetables
X,Y,Z = vegetables #unpacking the list into variables
print(X) #prints carrots only
print(type(vegetables)) #prints the data type of the variable vegetables which is a list

#casting is when you change the data type of a variable to another data type. For example, if you have a variable that is an integer and you want to change it to a string, you can use casting.
x = str(5) #casting 5 to a string
y = int("10") #casting "10" to an integer
z = float(3.14) #casting 3.14 to a float/decimal

#functions are a block of code that only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

def print_values():
    print(y) #this variable is global aka outside the function

def local_variable():
    local_var = "I am a local variable" #this variable is local aka inside the function
    print(local_var)

if 5 > 3:

    print(a, end=" ") #because of the end=" " it will print on the same line
    print(fact)

if 2 > 1: #bruh
        
        print("Fact is that", 2, "is greater than", 1) #statement is in "" and then in order to put the numbers in the statement we use commas to separate them

print_values()
local_variable() #hi