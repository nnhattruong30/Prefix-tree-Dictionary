# Create 

import os

path = os.path.join(os.getcwd(), "data/data.txt")
with open(path, "r") as f:
    x = f.readline()
    b = x.split()
    t = "".join(b)
    print(b)
    print(t)