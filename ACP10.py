def longest_consecutive_ones(n):
    # Convert the number to its binary representation and remove the '0b' prefix
    binary_representation = bin(n)[2:]
    # Split the binary string by '0' to find sequences of consecutive '1's
    consecutive_ones = binary_representation.split('0')
    # Find the length of the longest sequence of '1's
    longest_sequence = max(len(seq) for seq in consecutive_ones)
    return longest_sequence

# Example usage
number = int(input("Enter your number: "))
longest_ones_length = longest_consecutive_ones(number)
print("Longest consecutive 1’s length:", longest_ones_length)
