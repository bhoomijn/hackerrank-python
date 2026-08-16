
# nested_lists.py

n = int(input())   # number of students
students = []

for _ in range(n):
    name = input()              # student name
    grade = float(input())      # student grade (float for decimals)
    students.append([name, grade])

# extract all grades
grades = [s[1] for s in students]

# find lowest and second lowest
lowest = min(grades)
second_lowest = min([g for g in grades if g != lowest])

# collect names with second lowest grade
names = [s[0] for s in students if s[1] == second_lowest]

# sort alphabetically and print
for name in sorted(names):
    print(name)
