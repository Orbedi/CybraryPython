import operator as op

saved_string = ''

def remove_letter(): #Remove a selected letter from a string
    result = ''
    string = str(input("Enter the string: "))
    letter = str(input("Enter the letter: "))
    for char in string:
        result += char if char != letter else ''
    print("The result is: " + result)
    return result

def num_compare(): #Compare 2 numbers to determine the larger
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    result = num1 if op.ge(num1,num2) else num2
    print("The largest number is: %d" % result)

def print_string(): #Print the previously stored string
    print(saved_string)
    return

def calculator(): #Basic Calculator (addition, subtraction, multiplication, division)
    operation_list = [op.add, op.sub, op.mul, op.truediv]
    operation = calculator_menu()
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    result = operation_list[operation](num1,num2)
    print("The result is: %d" % result)
    return result

def calculator_menu():
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = int(input("Operation: ")) - 1
    if 0 <= int(operation) < 4:
        return operation
    else:
        print("Please, enter a correct value.")
        exit()

def accept_and_store(): #Accept and store a string
    global saved_string
    aux = saved_string
    string = input("Put the string: ")
    saved_string = string if isinstance(string, str) else aux

def main(): #menu goes here
    functions_list = [print_string,
                      accept_and_store,
                      num_compare,
                      calculator,
                      remove_letter]
    while True:
        print("OPTIONS:")
        print("1. Print string")
        print("2. Accept and store string")
        print("3. Compare 2 numbers")
        print("4. Calculator")
        print("5. Remove a letter")
        option = int(input("SELECT AN OPTION: ")) - 1
        if (0 <= option < 5):
            functions_list[option]()
        else: print("Please, enter a correct value.")
        print('\n====================================')

main()
