names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
upper_case_long_names = [name.upper() for name in names if len(name) > 5]
print(upper_case_long_names)

"""Original code would have to look like this (6 lines vs 3 lines)"""
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_names = []
# for name in names:
#     if len(name) > 4:
#         new_names.append(name.upper())
# print(new_names)
