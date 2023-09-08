# Function to check if a string is a palindrome (case-insensitive)
def is_palindrome(s):
    # Convert the string to lowercase for case-insensitive comparison
    s = s.lower()
    
    # Remove non-alphanumeric characters from the string
    s = ''.join(char for char in s if char.isalnum())
    
    # Compare the string with its reverse
    return s == s[::-1]

# Input the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    strstr = input()
    if is_palindrome(strstr):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
