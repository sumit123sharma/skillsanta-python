#python program to swap first and last value of a list

list_4=[]

num=int(input("enter the no. of elements in list:"))

for i in range(1,num+1):
    numbers=int(input("enter elements:"))
    list_4.append(numbers)

#swap first and last value by using the temp variable
temp=list_4[0]
list_4[0]=list_4[num-1]
list_4[num-1]=temp

print("list after swapping is : " , list_4)
