def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# Example usage
largest_number = int(input("Enter Largest number: "))
smallest_number = int(input("Enter Smallest number: "))
result = lcm(largest_number, smallest_number)
print("LCM is:", result)
