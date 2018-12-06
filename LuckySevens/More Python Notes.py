#shopping_list(0) = "2% milk"
#print(shopping_list)
#print(shopping_list[0])

# Looping through lists
#for item in shopping_list:
   # print(item)

'''
1. Make a list
2. change the 3rd thing on the list
3. print the item
4.print the full list
'''

#List = ["straw", "nut", "glass", "lime", "table", "chair", "Tonatiuh", "Kacchan", "Adam"]
#List[2] = "5&"
#print(List[2])
#print(List)

# new_list = {"eggs", "cheese", "oranges"}
# new_list[2] = "apples"
# print("The last thing in the list is %s" % new_list[len(new_list]  - 1)
# print(new_list)

 # Getting part of a list
 #print(new_list[1:4])
# print(new_list[1:])
 #print(new_list[:2])

 # Adding things to a list
#holiday_list = []
# holiday_list.append("Tacos")
# holiday_list.append("Bumblebee")
# holiday_list.append("Red Dead Redemption 2")
# print(holiday_list)

 # Notice this is object.method(Parameters)"

 # Removing things from a list
 # holiday_list.remove("Tacos")
# print(holiday_list)


#List = ["Cheese, Bacon, Eggs"]
#List[2] = "Milk"
#List.remove("Milk")


#brands = ("Apple", "Samsung", "HTC") # notice the parentheses
colors = ['blue', 'cyan', 'teal', 'red', 'green', 'orange', 'purple', 'clear', 'grey', 'black', 'white', 'pink', 'rose']
#print(len(colors))


# Find the index
print(colors.index("green"))

# Changing things into a list
string1 = "grey"
list1 = list(string1)
print(list1)


# Changing lists into strings


print("ree".join(list1))


for character in list1:
    if character == "r":
        # replace with a *
        current_index = list1.index(character)
        list1.pop(current_index)
        list1.insert(current_index, "*")