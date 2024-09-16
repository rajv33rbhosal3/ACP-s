def find_rightmost_set_bit_position(n):
    if n == 0:
        return -1  # No set bit in zero
    position = 1
    while (n & 1) == 0:
        n = n >> 1
        position += 1
    return position

# Example usage
number = int(input("Enter number: "))
position = find_rightmost_set_bit_position(number)
if position != -1:
    print(f"Position of the first set bit: {position}")
else:
    print("No set bit found.")
