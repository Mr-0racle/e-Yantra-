# Function to compute and print the required values for a given n
def compute_values(n):
    result = []
    for i in range(1, n):
        if i != 0:
            if i % 2 == 1:
                result.append(i * i)
            else:
                result.append(2 * i)
        else:
            result.append(i + 33)
    return result

# Input the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    n = int(input())
    values = compute_values(n)
    print(" ".join(map(str, values)))
