# Write a Python program to count the number of even and odd numbers from a series of numbers.


def check(num):
    global odd
    global even
    for i in num:
        if(i%2==0):
            even=even+1
        else:
            odd=odd+1
    print("Even is",even,"Odd is ",odd)


lst=[1,2,3,4,5,6,7,8,9,10]
check(lst) 

       