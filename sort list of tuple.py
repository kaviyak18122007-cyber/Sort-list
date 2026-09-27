# List of Tuples: (Name, Marks)
students = [("Arun", 85), ("Bala", 92), ("Chitra", 78), ("David", 88)]

# Marks base panni sort panna (Index 1)
sorted_by_marks = sorted(students, key=lambda x: x[1], reverse=True)

print("Top Performers (Highest to Lowest Marks):")
for rank, (name, marks) in enumerate(sorted_by_marks, 1):
    print(f"Rank {rank}: {name} - {marks} Marks")