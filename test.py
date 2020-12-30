import math


print("Nicholas was here")

a = 1
for a in range(10):
    print(a, end=", ")
print("done")

n = int(input("Enter a number n: "))

print("n = " + str(n))
print("n * 2 = " + str(n * 2))
print("n * n = " + str(n * n))
print("n / 2 = " + str(n / 2))
print("sqrt(n) = " + str(math.sqrt(n)))

if n < 10:
    print("It's less than 10")
elif n >= 20:
    print("It's 20 or more")
else:
    print("It's 10 up to 19")

if n % 2:
    print("the number is odd")
else:
    print("the number is even")

print("The End")




