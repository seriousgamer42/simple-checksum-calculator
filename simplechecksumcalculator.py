def simple_checksum(data):
    checksum = 0
    for char in data:
        checksum += ord(char)  # Add the ASCII value of each character
    checksum &= 0xFF  # Keep only the least significant 8 bits
    return checksum

# Example usage:
data = input("Please enter a phrase: ")
checksum = simple_checksum(data)
print(f"Checksum: {checksum}")
