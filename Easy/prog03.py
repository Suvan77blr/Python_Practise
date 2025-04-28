# Getting MAX and MIN from a list.

import numpy as np

# Generating a random list of 8 nos between 0 and 100.
size, high = 8, 100
lst = np.array(np.random.rand(size)*high, dtype="int32")

low, high = lst[0], lst[0]      # Variables for lowest and highest.

for num in lst:
    if num > high:
        high = num
    
    if num < low:
        low = num
# end-for

print(f"Random List : {lst}")
print(f"Lowest value : {low}")
print(f"Highest value : {high}")