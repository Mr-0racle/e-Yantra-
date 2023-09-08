# Function to perform operations on the list
def perform_operations(length, numbers):
    # Step 1: Print the list in reverse order
    reverse_list = numbers[::-1]
    print(" ".join(map(str, reverse_list)))

    # Step 2: Print every third number with 3 added to it
    modified_third_numbers = [numbers[i] + 3 for i in range(0, length, 3)]
    print(" ".join(map(str, modified_third_numbers)))

    # Step 3: Print every fifth number with 7 subtracted from it
    modified_fifth_numbers = [numbers[i] - 7 for i in range(0, length, 5)]
    print(" ".join(map(str, modified_fifth_numbers)))

    # Step 4: Sum of all numbers with an index between 3 and 7 (inclusive)
    sum_of_range = sum(numbers[3:8])
    print(sum_of_range)

# Input the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    length = int(input())
    numbers = list(map(int, input().split()))
    perform_operations(length, numbers)
