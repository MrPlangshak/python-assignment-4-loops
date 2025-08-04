
"""
Task: Hundred Student Records - Filtering with Loops and Conditionals

Scenario:
The Federal University of Jos wants to analyze the performance of its students 
after conducting a nationwide online assessment. 
They have exactly 100 student records in the system.

Each student record includes:
- student_id (integer)
- name (string)
- score (0 - 100)

A sample of the dataset looks like this:

students = [
    {"id": 1, "name": "Alice", "score": 78},
    {"id": 2, "name": "Bob", "score": 45},
    {"id": 3, "name": "Charlie", "score": 92},
    ...
]

The academic board wants to classify the students into 3 separate groups 
based on their scores:

1. High Performers: score >= 70
2. Average Performers: 50 <= score < 70
3. Low Performers: score < 50

Requirements:
1. Use a loop to iterate through all student records.
2. Use conditionals to filter and classify students into 3 separate groups.
3. Each group should be identified by its name (Group Name).
4. Each group should use `student_id` as the key and a tuple `(name, score)` as the value.
5. Print the number of students in each category as a summary report.
6. print each category(3)

Example Output:
High Performers: 300,245
Average Performers: 400,512
Low Performers: 299,243


e.g. 
All High Performers: [{1: ("student1", 100)}, {32: ("student32", 90)}, ..... continously]
All Average Performers: [{1: ("student1", 100)}, {32: ("student32", 90)}, ..... continously]
All Low Performers: [{1: ("student1", 100)}, {32: ("student32", 90)}, ..... continously]
"""
students = [
    {'id': 1, 'name': 'Godiya', 'score': 68},
    {'id': 2, 'name': 'Daisy', 'score': 86},
    {'id': 3, 'name': 'Dorcas', 'score': 44},
    {'id': 4, 'name': 'M P', 'score': 60},
    {'id': 5, 'name': 'Thankgod', 'score': 1},
    {'id': 6, 'name': 'Morgak', 'score': 25},
    {'id': 7, 'name': 'FifthSon', 'score': 31},
    {'id': 8, 'name': 'Dakshak', 'score': 85},
    {'id': 9, 'name': 'Praise', 'score': 53},
    {'id': 10, 'name': 'Tunde', 'score': 33},
    {'id': 11, 'name': 'Ifeoma', 'score': 75},
    {'id': 12, 'name': 'Sani', 'score': 2},
    {'id': 13, 'name': 'Oluchi', 'score': 95},
    {'id': 14, 'name': 'Yakubu', 'score': 36},
    {'id': 15, 'name': 'Kemi', 'score': 55},
    {'id': 16, 'name': 'Chuka', 'score': 57},
    {'id': 17, 'name': 'Hauwa', 'score': 97},
    {'id': 18, 'name': 'Bolaji', 'score': 44},
    {'id': 19, 'name': 'Nneka', 'score': 81},
    {'id': 20, 'name': 'Bello', 'score': 20},
    {'id': 21, 'name': 'Temitope', 'score': 65},
    {'id': 22, 'name': 'Obinna', 'score': 68},
    {'id': 23, 'name': 'Zainab', 'score': 41},
    {'id': 24, 'name': 'Uchechi', 'score': 16},
    {'id': 25, 'name': 'Gambo', 'score': 18},
    {'id': 26, 'name': 'Ayodele', 'score': 88},
    {'id': 27, 'name': 'Chiamaka', 'score': 59},
    {'id': 28, 'name': 'Fatima', 'score': 89},
    {'id': 29, 'name': 'Segun', 'score': 12},
    {'id': 30, 'name': 'Adaeze', 'score': 13},
    {'id': 31, 'name': 'Alhassan', 'score': 87},
    {'id': 32, 'name': 'Afolabi', 'score': 20},
    {'id': 33, 'name': 'Onyeka', 'score': 43},
    {'id': 34, 'name': 'Omolara', 'score': 36},
    {'id': 35, 'name': 'Farouk', 'score': 47},
    {'id': 36, 'name': 'Kehinde', 'score': 14},
    {'id': 37, 'name': 'Amarachi', 'score': 14},
    {'id': 38, 'name': 'Bashir', 'score': 61},
    {'id': 39, 'name': 'Ijeoma', 'score': 86},
    {'id': 40, 'name': 'Abubakar', 'score': 87},
    {'id': 41, 'name': 'Bamidele', 'score': 24},
    {'id': 42, 'name': 'Efe', 'score': 61},
    {'id': 43, 'name': 'Nnamdi', 'score': 69},
    {'id': 44, 'name': 'Sola', 'score': 56},
    {'id': 45, 'name': 'Halima', 'score': 47},
    {'id': 46, 'name': 'Odion', 'score': 27},
    {'id': 47, 'name': 'Chinwe', 'score': 84},
    {'id': 48, 'name': 'Yusuf', 'score': 71},
    {'id': 49, 'name': 'Blessing', 'score': 4},
    {'id': 50, 'name': 'Taiwo', 'score': 43},
]

high_performers = []
average_performers = []
low_performers = []

for student in students:
    sid = student["id"]
    name = student["name"]
    score = student["score"]

    if score >= 70:
        high_performers.append({sid: (name, score)})
    elif score >= 50:
        average_performers.append({sid: (name, score)})
    else:
        low_performers.append({sid: (name, score)})

#summary
print("High Performers:", len(high_performers))
print("Average Performers:", len(average_performers))
print("Low Performers:", len(low_performers))

#Show all students by group
print("\nAll High Performers:", high_performers)
print("\nAll Average Performers:", average_performers)
print("\nAll Low Performers:", low_performers)

