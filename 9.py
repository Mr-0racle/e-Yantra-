# Function to generate the arithmetic progression
def generate_AP(a1, d, n):
    AP = [a1 + (i * d) for i in range(n)]
    return AP

# Input the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    a1, d, n = map(int, input().split())

    # Generate the A.P. series
    AP_series = generate_AP(a1, d, n)
    print(" ".join(map(str, AP_series)))

    # Find squares of terms in the series using lambda and map
    squares = list(map(lambda x: x**2, AP_series))
    print(" ".join(map(str, squares)))

    # Compute the sum of squares of terms using reduce
    from functools import reduce
    sum_of_squares = reduce(lambda x, y: x + y, squares)
    print(sum_of_squares)
