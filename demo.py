#Reverse of a Number
num = int (input("123456789"))
rev = 0
temp = num
while(num!=0):
    digit = num % 10
    rev = rev*10 + digit
    num = num//10

print ("The reverse of the number:",temp," is:" , rev)