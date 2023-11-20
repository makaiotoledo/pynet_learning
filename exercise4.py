line = "Processor board ID FAL127990LA"

check = "Processor board ID" in line
print(f"\nMembership check should be True|False: {check}")

_, _, _, serial_number = line.split()
print("\nCall .split() and assign output to four variables:")

print(serial_number)
