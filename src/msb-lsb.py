inp = input("Enter a binary number: ")
try:
    pro = int(inp,2)
except ValueError:print("Error!")
else:
    print(f"The MSB [Most Significant Bit] is {inp[0]} and the LSB [Least Significant Bit] is {inp[-1]}")