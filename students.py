import random

# Generate 100 student records
students = [
    {
        "id": i + 1,
        "name": f"Student{i+1}",
        "score": random.randint(0, 100)
    }
    for i in range(100)
]

print(students);