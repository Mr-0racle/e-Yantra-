import math

# Function to compute Euclidean distance between two points
def compute_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distance, 2)

# Input the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    distance = compute_distance(x1, y1, x2, y2)
    print(f"Distance: {distance}")
