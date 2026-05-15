students = [
    {"name": "KAI", "english": 75, "maths" : 42, "science" : 85},
    {"name": "TYSON", "english": 82, "maths" : 24, "science" : 44},
    {"name": "RAY", "english": 99, "maths" : 88, "science" : 75},
    {"name": "MAX", "english": 90, "maths" : 75, "science" : 74},
    {"name": "DAISI", "english": 92, "maths" : 65, "science" : 93}
]

# Hash map to store scores
student_scores = {}

# Process dataset
for student in students:
    name = student["name"]
    english_mark = student["english"]
    maths_mark = student["maths"]
    science_mark = student["science"]

    if name not in student_scores:
        student_scores[name] = []

    student_scores[name].extend((english_mark,maths_mark,science_mark))



print(student_scores)



print("Average Scores:")
top_student = ""
highest_avg = 0

for name, scores in student_scores.items():
    avg = sum(scores) / len(scores)

    print(name, "->", avg)

    if avg > highest_avg:
        highest_avg = avg
        top_student = name

print("\nTop Student:", top_student)
print("Highest Average:", highest_avg)