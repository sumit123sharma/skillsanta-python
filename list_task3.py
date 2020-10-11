#python script to merge two lists and sort it
list1=[]
list2=[]

num1=int(input("enter the no. of elements in list1:"))

for i in range(1,num1+1):
    numbers1=int(input("enter elements in list1:"))
    list1.append(numbers1)

#same for list2

num2=int(input("enter the no. of elements in list2:"))

for i in range(1,num2+1):
    numbers2=int(input("enter elements in list2:"))
    list2.append(numbers2)

# merge lists by + operator

new_list=list1+list2
new_list.sort()
print("sorted list is:" , new_list)

