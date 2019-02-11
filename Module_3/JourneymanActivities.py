import socket

'''1.1) Take two arguments, a list and an integer. The list is a series 
of strings; one of those strings will be the filename, the others will 
be the file contents. The integer is the location in the list of the file 
name. (Write each string to a separate line)

list:
a 0 <-contents
b 1 <-contents
c 2 <-contents
d 3 <-contents
e 4 <- filename
f 5 <-contents

item:
4

'''
def journeyman1(str_list , item):
    filename = str(str_list[item])
    file = open(filename,"w+")
    for index,content in enumerate(str_list):
        if index != item: file.write(content)
    file.close()
    return


'''1.2) Write a function which takes a single integer as an argument and 
returns the sum of every integer up to and including that number, use a 
generator.'''

def sum_generator(final_num):
    for n in range(final_num+1):
        yield (n)

def journeyman2(final_num):
    return sum(sum_generator(final_num))


'''1.3) Write a python script which connects to the included server 
on port 50001 and returns the message it receives.'''
def journeyman3():
    return


'''1.4) Create a class called person, with height, weight, hair color, 
and eye color fields, then implement it to describe yourself.'''
def journeyman4():
    return
    

def main():
    print(journeyman2(3))

main()
