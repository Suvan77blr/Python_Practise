import numpy as np

# Generating a random list of size 10, with digits between 0 and 100.
size, high = 10, 100
lst = np.array(np.random.rand(size)*high, dtype="int32")

low, high = lst.min(), lst.max()
range = high - low

print(f"Random List : {lst}")
print(f"Lowest & Highest Values : {low} & {high}")
print(f"Highest - Lowest : {range}")