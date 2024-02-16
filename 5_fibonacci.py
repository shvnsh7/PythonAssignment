# V.Write a program to print fibonacci series for the given input occurence (if user gives i\p as 6 then it should print series till 6th number)
# FiBoNACCI series
# 0 1 1 2 3 5 8 13 21
 
# Input: 6, Output: 0 1 1 2 3 5
# Input: 10, Output: 0 1 1 2 3 5 8 12 21 34


# n=int(input("Enter the number "))
# n1,n2=0,1
# count=0

# if n<=0:
#     print("Enter a positive intiger")

# elif n==1:
#     print("1")

# else:
#     while count <n:
#         print(n1)
#         nth=n1+n2
#         n1=n2
#         n2=nth
#         count+=1



def fibonacci(n):
    #n=int(input("Enter the number "))
    n1,n2=0,1
    count=0

    if n<=0:
        print("Enter a positive intiger")

    elif n==1:
        print("1")

    else:
        while count <n:
            print(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1

print(fibonacci(6))



