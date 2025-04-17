# Create an empty list
my_list = []

# (Optional) Let the user input the initial elements
print("Enter initial elements separated by spaces (e.g., 10 20 30 40):")
initial_elements = input().split()  # Splits input into a list of strings
my_list = [int(num) for num in initial_elements]  # Convert strings to integers

# If no input was provided, default to [10, 20, 30, 40]
if not my_list:
    my_list = [10, 20, 30, 40]
    print("Using default list:", my_list)
else:
    print("Your starting list:", my_list)

# Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print("After inserting 15:", my_list)

# Extend with [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending:", my_list)

# Remove the last element
my_list.pop()
print("After removing last element:", my_list)

# Sort the list
my_list.sort()
print("After sorting:", my_list)

# Find index of 30
try:
    index_of_30 = my_list.index(30)
    print("Index of 30:", index_of_30)
except ValueError:
    print("30 is not in the list!")

# Final list
print("Final list:", my_list)
