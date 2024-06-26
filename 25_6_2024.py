# a = 10
# b = a
# a = 4
# print(a,b)
# name = input("Enter of name:")
# print("hello:",name)
# number = 5
# print(number ** 2)
# number = float(input("Enter number:"))
# print(number//2)
num = int(input("Enter a number: "))
print((num//100) + ((num//10)%10) + (num%10))
print((num//100 + (num//10)%10 + num%10) //3)
print((num//100 + (num//10)%10 + num%10) %3)
print(bool(num//100 + (num//10)%10 + num%10) %3 == 0)

