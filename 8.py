# Function to find students with the maximum score
def find_max_score_students(students):
    max_score = -1
    max_score_students = []

    for student, score in students:
        if score > max_score:
            max_score = score
            max_score_students = [student]
        elif score == max_score:
            max_score_students.append(student)

    return max_score_students

# Input the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    N = int(input())
    student_scores = []

    # Read student names and scores
    for _ in range(N):
        name, score = input().split()
        score = int(score)
        student_scores.append((name, score))

    # Find students with the maximum score
    max_score_students = find_max_score_students(student_scores)

    # Sort the names in ascending alphabetical order
    max_score_students.sort()

    # Print the names
    for student in max_score_students:
        print(student)
