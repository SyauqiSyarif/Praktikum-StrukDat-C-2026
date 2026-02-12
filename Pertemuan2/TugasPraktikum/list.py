# Access List Items

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative indexing

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Change Item Value

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Insert Items

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Extend Items

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove Specified Item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Loop List

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Range/Len
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# List Comperhension 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# Sort List

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Copy List

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Join List

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

