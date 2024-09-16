def reverse_bits(num):
    # Convert the number to binary and remove the '0b' prefix
    binary_str = bin(num)[2:]
    # Reverse the binary string
    reversed_binary_str = binary_str[::-1]
    # Convert the reversed binary string back to a decimal number
    reversed_num = int(reversed_binary_str, 2)
    return reversed_num

# Example usage
original_number = int(input("Enter your original number: "))
reversed_number = reverse_bits(original_number)
print(f"Reversed Number: {reversed_number}")
