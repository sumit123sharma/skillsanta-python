#python program to find the second largest no. in a list

list2=[]
num=int(input("enter the no. of elements:"))

for i in range(1,num+1):
    numbers=int(input("enter numbers"))
    list2.append(numbers)

#now sort the list
list2.sort()
#print the second largest by negative indexing method
print("second largest no. is:" , list2[-2])