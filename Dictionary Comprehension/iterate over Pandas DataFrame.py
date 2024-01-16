import random

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(key, value[random.randint(1, 2)])

import pandas as pd

# loop through a DataFrame:
data_frame = pd.DataFrame(student_dict)
# for (key, value) in data_frame.items():
#     print(key)
#     print(value)

# loop through each row of a DataFrame:
for (index, row) in data_frame.iterrows():
    print(row.score)