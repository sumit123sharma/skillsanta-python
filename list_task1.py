#python program to find largest no in a list
#create an empty list
list=[]
num=int(input("enter the no. of elements:"))

for i in range(1,num+1):
    numbers=int(input("enter numbers:"))
    list.append(numbers)

#print the largest no. by max method
print("largest element is:" , max(list))

