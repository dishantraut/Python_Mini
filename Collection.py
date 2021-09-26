# https://www.youtube.com/playlist?list=PLyb_C2HpOQSDSFkAp8pqyk0m9MG2BwZKC
# * Collection Module

from timeit import default_timer as timer
import collections

# -----------------------------------------------------------------------------

# * Counter :- create a frequency table
a = [11,12,13,14,14,11,12,13]
a = ["hi","hello","hi","hello","hi","hello","hi","hello"]

print(collections.Counter(a))

# -----------------------------------------------------------------------------

name = "DishantRajendraRaut"
d = dict()
for c in name:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1

print(d)


# * Default value is 0
e = collections.defaultdict(int)
# * To set default value as 2
# e = collections.defaultdict(lambda:2)

for d in name:
    e[d] += 1

print(e)
print(e['z']) # If key is not present the default values is zero incase of lambda it will be 2

# -----------------------------------------------------------------------------

scores = [('Nikhil',6), ('Dishant',2), ('Ritesh',3), ('Rahul',8),]

d1 = dict()
for name, score in scores:
    d1[name] = score

print(d1)
print(d1.keys())
print(d1.values())

odict = collections.OrderedDict(scores)
print(odict.keys())
print(odict.values())

# -----------------------------------------------------------------------------

d2 = {'a':1, 'b':2, 'c':3}
d3 = {'e':4, 'f':5, 'g':6}

dict1 = collections.ChainMap(d3, d2)
print(dict1['e'])
print(dict1['a'])
