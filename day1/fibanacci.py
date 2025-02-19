# Write a program to calculate Fibonacci sequence.
def fibonacci(val):
    first=0
    second=1
    sum=0
    for x in range(0,val):
        sum+=second
        print(first,"  ",second,"   ",sum)
        temp=first+second
        first=second
        second=temp
    return sum


val=int(input("enter the number : "))
print("sum of fibonacci series till index ",val," is ",fibonacci(val))