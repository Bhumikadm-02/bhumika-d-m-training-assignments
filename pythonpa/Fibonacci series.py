#user input 
n = int(input("Input a number: "))

#initialization
a=0
b=1

for i in range(n):
    print(a)
    a, b = b, a + b


