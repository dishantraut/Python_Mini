# https://stackabuse.com/introduction-to-pythons-collections-module/

"""
Counter() function can take a dictionary as an argument. 
In this dictionary, the value of a key should be the 'count' of that key.

"""
from collections import OrderedDict
from collections import defaultdict
from collections import Counter


list = [1,2,3,4,1,2,6,7,3,8,1]
print('\n#Counter()')
print(Counter(list))

# OR

""" cnt is an object of Counter class which is a subclass of dict. So it has all the methods of dict class """
cnt = Counter(list)
print('\n#cnt')
print(cnt[3])

""" 
most_common function returns a list, which is sorted based on the count of the elements. 
1 has a count of three, therefore it is the first element of the list. 
"""
print('\n#cnt.most_common()')
print(cnt.most_common())


"""
The names_list includes a set of names which repeat several times. 
The split() function returns a list from the given string. 
It breaks the string whenever a white-space is encountered and returns words as elements of the list. 
In the loop, each item in the list is added to the defaultdict named as count and initialized to 0 based on default_factory. 
If the same element is encountered again, as loop continues, count of that element will be incremented.
"""
count = defaultdict(int)
names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
for names in names_list:
    count[names] +=1
print('\n#defalutdict()')
print(count)

"""
Create a OrderedDict
You can create an OrderedDict object with OrderedDict() constructor. 
In the following code, You create an OrderedDict without any arguments. After that some items are inserted into it.
"""
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print('\n#OrderedDict()')
print(od)

for key, value in od.items():
    print(key, value)
    
print('\n#All Together')
list = ["a","c","c","a","b","a","a","b","c"]
cnt = Counter(list)
od = OrderedDict(cnt.most_common())
for key, value in od.items():
    print(key, value)
