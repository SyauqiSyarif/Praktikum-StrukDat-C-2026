
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Access Set Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Add Set Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#Remove Set Items
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# Loop Sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Join Sets 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# Frozen Sets

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

