line = "Processor board ID FAL127990LA"

_, _, _, serial_number = line.split()
print("\nCall .split() and assign output to four variables:")
print(serial_number)

print("\nCall .split() and assign output to a list and a variable:")
*junk, serial_number = line.split()
print(serial_number)

print("\nCall .split() and assign output to a list:")
words = line.split()
serial_number = words[-1]
print(serial_number)
