from itertools import groupby

inp = input("Enter binary: ")

# Compress
processed = [''.join(g) for k, g in groupby(inp)]
result = []
for i in processed:
    if len(i) > 2:
        result.append(f"{len(i)}{i[0]}")
    else:
        result.append(i)
print("Compressed version is","".join(result))

# Decompress
decompressed = []
for i in result:
    x = int(i[0])
    if x>1:
        decompressed.append(x*i[1])
    else:
        decompressed.append(i)

print("The decompressed version is","".join(decompressed))