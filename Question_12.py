# Q12.Python program to check whether the given number is prime or not.

num = int(input("Enter a number : "))
flag = 0
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = 1
            break
if flag==1:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")