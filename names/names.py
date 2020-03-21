import time
from binary_search_tree import BinarySearchTree

# the original runtime of the for loops provided is O(n^2)
# my plan is to add one list to a bst and iterate through the other list checking if the bst contains that name
# if contains == true add to dupes


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# store one list of names in a binary search tree
# iterate through the other list checking to see if the bst contains the name
# if true add to dupes
names1bst = BinarySearchTree(None)
for name_1 in names_1:
    names1bst.insert(name_1)
    for name_2 in names_2:
        if names1bst.contains(name_2):
            duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
