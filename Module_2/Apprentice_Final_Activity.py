import operator as op

saved_string = ''

def remove_letter(letter, string): #Remove a selected letter from a string
    iterations = op.countOf(string, letter)
    result = string
    while iterations > 0:
        iterations -= 1
        result = op.delitem(letter,op.indexOf(result, letter))
    return string

def num_compare(): #Compare 2 numbers to determine the larger
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    result = num1 if op.ge(num1,num2) else num2
    print("The largest number is: %d" % result)

def print_string(): #Print the previously stored string
    print(saved_string)
    return

def calculator(): #Basic Calculator (addition, subtraction, multiplication, division)
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = str(input("Operation: "))
    if int(operation) > 0 and int(operation) < 5:
        num1 = int(input("Number 1: "))
        num2 = int(input("Number 2: "))
        if operation == '1':
            result = op.add(num1,num2)
        elif operation == '2':
            result = op.sub(num1,num2)
        elif operation == '3':
            result = op.mul(num1,num2)
        elif operation == '4':
            result = op.truediv(num1,num2)
        print("The result is: %d" % result)
    else: print("Please, enter a correct value.")

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
