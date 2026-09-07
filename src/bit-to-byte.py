import hexotools

choice = hexotools.multiChoice("Bytes to bits","Bits to bytes")
inp = int(input("Enter value to be converted: "))
if choice[0] == 0:print(f"{inp} = {inp*8}")
else:print(f"{inp} = {inp/8:g}")