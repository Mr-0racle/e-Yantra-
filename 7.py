# Function to convert decimal to binary recursively
def dec_to_binary(n, bits):
    if n == 0:
        return '0' * (bits - 1) + '0'
    elif n == 1:
        return '0' * (bits - 1) + '1'
    else:
        return dec_to_binary(n // 2, bits - 1) + str(n % 2)

# Input the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    n = int(input())
    binary = dec_to_binary(n, 8)
    print(binary)
