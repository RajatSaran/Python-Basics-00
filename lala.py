for num in range(0,9):
    if num%2==0:
        print(num)


for num in range (0,9):
    if num%2!=0:
        print(num)
for num in range(10,0,-1):
    print(num)

print("enter no 1")
num1 = input()
print("enter no 2")
num2= input()
try:
    print ("the sum of these no is",
       int(num1)+int(num2))
except Exception as e:
    print (e)

print ("this line is very important")




input_list = [1, 2, 6, 7, 9]
for i in range(1,10):
    if i in input_list:
        continue
    print(i)



year=int(input())
    
if ((year % 400 == 0) or (year % 100 != 0)and(year%4 ==0)):
 print("True")

else:
    print("False")


def is_leap(year):
    leap = False
    
    if(year % 400 == 0)and(year % 100 == 0):
     leap = True
    
    elif (year % 4 == 0):
      leap = True

    else:
       pass
    return leap