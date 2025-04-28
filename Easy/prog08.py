# Finding average of all elements of a list.

import numpy as np

# Random size btn 1 and 10.
size_low, size_high = 1, 10
random_size = np.random.randint(size_low, size_high+1, size=1, dtype="int32")[0]

# Random list of generated size.
low, high = 0, 100
list_nums = np.random.randint(low, high+1, size=random_size, dtype="int32")

sum_total = list_nums.sum()
avg = sum_total / len(list_nums)

print(f"Random Size : {random_size}")
print(f"List : {list_nums}")
print(f"Sum : {sum_total}")
print(f"Average : {avg:.3f}")