x,y,z,a = map(int,[
    input("How many reports: "),
    input("Size of each report (in bytes): "),
    input("How many images: "),
    input("File size of each photograph (in bytes): ")
])
b=x*y+z*a

print(f"Size in total is {b} bytes, or {b/1000} kb or {b/1_000_000} mb")