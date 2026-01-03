# # Dictionary Example
# student = {
#     "name": "Riya",
#     "age": 22,
#     "course": "B.Tech",
#     "year": 4
# }

# # Access
# print(student["name"])
# print(student.get("roll_no", "Not Assigned"))

# # Add / Update
# student["roll_no"] = 101
# student["age"] = 23
# student.setdefault("hobby", "Reading")

# # Delete
# student.pop("course")
# student.pop("non_exist_key", "No Key")
# del student["year"]
# # student.clear()  # Uncomment to empty the dictionary

# # Other functions
# print(student.keys())
# print(student.values())
# print(student.items())
# print(len(student))
# copy_student = student.copy()
# new_student = dict.fromkeys(["name","age","city"], "Unknown")

# # Looping
# for k, v in student.items():
#     print(k, ":", v)

# for k in student:
#     print(k)

# for v in student.values():
#     print(v)

# # Sorting by keys
# for k in sorted(student):
#     print(k, student[k])

# # Nested Dictionary
# classes = {
#     "class1": {"teacher": "Mr. A", "students": 20},
#     "class2": {"teacher": "Ms. B", "students": 25}
# }

# for cls, details in classes.items():
#     print(cls)
#     for k, v in details.items():
#         print(" ", k, "=", v)
