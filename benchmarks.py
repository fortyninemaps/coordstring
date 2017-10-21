import timeit
import numpy as np
from coordstring import CoordString

def np_init(data):
    return np.asarray(data)

def cs_init(data):
    return CoordString(data)

def py_init(data):
    return [(float(i),float(j)) for (i,j) in data]

print("Initialization")
init_data = [(i,j) for i in range(1000) for j in range(100)]
print(timeit.timeit("py_init(init_data)", number=100, globals=globals()))
print(timeit.timeit("np_init(init_data)", number=100, globals=globals()))
print(timeit.timeit("cs_init(init_data)", number=100, globals=globals()))

print("Indexing a position")

py_data = py_init(init_data)
np_data = np_init(init_data)
cs_data = cs_init(init_data)

print(timeit.timeit("py_data[1700]", number=10000000, globals=globals()))
print(timeit.timeit("np_data[1700]", number=10000000, globals=globals()))
print(timeit.timeit("cs_data[1700]", number=10000000, globals=globals()))

print("Slicing")

print(timeit.timeit("py_data[1700:2000]", number=1000000, globals=globals()))
print(timeit.timeit("np_data[1700:2000]", number=1000000, globals=globals()))
print(timeit.timeit("cs_data.slice(1700, 2000)", number=1000000, globals=globals()))

print("Bounding box")

print(timeit.timeit("(min(x for x,_ in py_data), min(y for _,y in py_data),"
                    " max(x for x,_ in py_data), max(y for _,y in py_data))",
                    number=500, globals=globals()))
print(timeit.timeit("(np_data[:,0].min(), np_data[:,1].min(),"
                    " np_data[:,0].max(), np_data[:,1].max())",
                    number=500, globals=globals()))
print(timeit.timeit("cs_data.bbox()", number=500, globals=globals()))

