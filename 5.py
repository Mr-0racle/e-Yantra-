# Function to count and print the lengths of words in a string
def count_word_lengths(input_string):
    # Remove the "@" at the beginning of the string
    input_string = input_string[1:]
    
    # Split the string into words using space as the delimiter
    words = input_string.split()

    # Calculate the lengths of each word and store them in a list
    word_lengths = [str(len(word)) for word in words]

    # Join the lengths with commas and print the result
    result = ",".join(word_lengths)
    print(result)

# Input the number of test cases
T = int(input())


for _ in range(T):
    input_string = input()
    count_word_lengths(input_string)
