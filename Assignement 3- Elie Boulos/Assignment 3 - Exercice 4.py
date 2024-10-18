

list1=[]
additional=True
while additional:
    number=int(input("Enter a number"))
    add_more=input("do you want to add new number? y/n").lower()
    if add_more!="y":
        additional=False
    list1.append(number)   
print(list1)
list1.sort()
print(list1)

start=0
end=len(list1)-1

def value_added(list1, target, start, end):
    if start > end:
        return start 
    mid = (start + end) // 2
    if list1[mid] == target:
        return mid  
    elif list1[mid] > target:
        return value_added(list1, target, start, mid - 1)
    else:
        return value_added(list1, target, mid + 1, end)

value = int(input('enter the number you want to add'))

def insert_into_sorted_list(sorted_list, value):
    index = value_added(sorted_list, value, 0, len(sorted_list) - 1)
    sorted_list.insert(index, value)
    
insert_into_sorted_list(list1, value)
print(list1)   