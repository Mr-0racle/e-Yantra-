# Function to generate the star and hash pattern
def generate_pattern(N):
    for i in range(N):
        # Calculate the number of stars and hashes for this row
        stars = N - i
        hashes = stars // 5
        remaining_stars = stars % 5

        # Create the pattern for this row
        pattern = '*' * (stars - remaining_stars) + '#' * remaining_stars

        # Print the pattern for this row
        print(pattern)

# Input the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    N = int(input())
    generate_pattern(N)
