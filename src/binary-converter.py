# Unit chart

unitBase = {
    ("b","bit","bits"):1,
    ("nibble","nibble"):4,
    ("B","byte","bytes"):8,

    ("kb","kilobyte","kilobytes"):8e+3,
    ("mb","megabyte","megabytes"):8e+6,
    ("gb","gigabyte","gigabytes"):8e+9,
    ("tb","terabyte","terabytes"):8e+12,
    ("pb","petabyte","petabytes"):8e+15,

    ("kib","kibibyte","kibibytes"):8*1024,
    ("mib","mebibyte","mebibytes"):8*1024**2,
    ("gib","gibibyte","gibibytes"):8*1024**3,
    ("tib","tebibyte","tebibytes"):8*1024**4,
    ("pib","pebibyte","pebibytes"):8*1024**5,
}

# Unsimplify unit chart

unitMap = {}
for k,v in unitBase.items():
    for i in k:
        unitMap[i] = v

# Main logic

inp = input("Enter value you are converting from (e.g. 1 gigabyte): ").lower().split()
to = input("Enter what you are converting to (e.g. megabytes): ").lower()

processing = float(inp[0])*unitMap[inp[1]]
processed = processing/unitMap[to]
print(f"{inp[0]} {inp[1]} = {processed:g} {to}")