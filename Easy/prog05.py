# Marks & Percentage from a LIST.

import numpy as np

# Assuming '30' as maximum marks & taking 5 subjects.
max_marks, subject_count = 30, 5

# Randomly generating the marks for the '5' subjects.
marks_list = np.random.randint(0, max_marks-1, size=subject_count, dtype="int32")

sum_total_marks = marks_list.sum()
max_marks_total = max_marks * subject_count

percentage = (sum_total_marks / max_marks_total) * 100
print(f"Marks List : {marks_list}")
print(f"Percentage : {percentage:.2f}%")