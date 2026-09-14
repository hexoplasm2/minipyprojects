# Unfinished

inp = input("Enter value you are converting with suffix (e.g. 1 gigabyte): ").lower().split()
to = input("Enter what you are converting to: ").lower()

# To bytes
if inp[1] in ("gigabyte","gigabyte","gb"):
    processing = float(inp[0])*8e+9
elif inp[1] in ("megabyte","megabytes","mb"):
    processing = float(inp[0])*8e+6

# To final
if to in ("megabyte","megabytes","mb"):
    processing/=8e+6
elif to in ("gigabyte","gigabytes","gb"):
    processing/=8e+9


print(f"{inp[0]} {inp[1]} = {processing:g} {to}")