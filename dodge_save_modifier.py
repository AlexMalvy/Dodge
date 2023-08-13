import pickle
import os
import sys

file = None

with open("dodge_save.txt", "rb") as f:
    file = pickle.load(f)

for entry in file:
    print(entry)
    print("")

with open("dodge_save.txt", "wb") as f:
    pickle.dump(file, f)