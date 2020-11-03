import cmath
def show_menu():
    print("Enter 0 to chek the palindrome")
    print("Enter 1 to chek is prime or not")
    print("Enter 99 to Exit")
def is_prime(num):
    f=1
    if num==1:
        print('not prime')
    else:
        for count in range(2,num):
            if(num%count==0):
                f=0
        if f == 1:
            print('is prime')
        else:
            print('not prime')

def is_plandrom(str):
    str2=str[::-1]
    f=1
    for x in range(0,len(str)-1):
        if str2[x]!=str[x]:
            f=0
    if f==1:
        print('is palindrome')
    else:
        print('not palindrome')
n=2
while n!=99:
    show_menu()
    n = int(input())
    if n==0:
        str=input('Enter the word')
        is_plandrom(str)
    elif n==1:
        num = int(input('Enter the number'))
        is_prime(num)
    elif n!=99:
        print('enter a correct number')





