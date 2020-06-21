
a , *b = 50 , 60 , 70
print(a)
print(b)
print(type(a))
print(type(b))

a = b = c = 50
print(a,b,c)
print(type(a))
print(type(b))
print(type(c))

a , b = 50 , 60
print(a,b)a , b = b , a
print("After swapping",a,b)

my_list = ['This' , 'is' , 'a' , 'string' , 'in' , 'Python']
my_string = " ".join(my_list)
print(my_list)

a = 15
if (10 < a < 20):
    print("Hi")

my_list = [1,2,3,1,1,4,2,1]
most_frequent = max(set(my_list),key=my_list.count)
print(most_frequent)

# Find Occurrence of all elements in list
from collections import Counter
my_list = [1,2,3,1,4,1,5,5]
print(Counter(my_list))

# Create Number Sequence with range
my_list = list(range(2,20,2))
print(my_list)

# List Comprehension
# new_list = [expression for item in iterable (if conditional)]
square_list = [x**2 for x in range(1,10)]
print(square_list)

# To convert Mutable to Immutable
my_list = [1,2,3,4,5]
my_list = frozenset(my_list)
my_list[3]=7
print(my_list)

# Apply Function to all elements of List
my_list = ["felix", "antony"]
new_list = map(str.capitalize,my_list)
print(list(new_list))

# Merge two dictionaries
dict_1 = {'One':1, 'Two':2}
dict_2 = {'Two':2, 'Three':3}
dictionary = {**dict_1, **dict_2}
print(dictionary)

# Combine to list into a dictionary
list_1 = ["One","Two","Three"]
list_2 = [1,2,3]
dictionary = dict(zip(list_1, list_2))
print(dictionary)

# Get Execution time
import time
start = time.process_time()
for x in range(1000):
    pass
end = time.process_time()
total = end - start
print(total)
