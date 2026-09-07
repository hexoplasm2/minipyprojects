# Unfinished

inp = input("Enter value you are converting with suffix (e.g. 1 megabyte): ")
split = inp.split()


match input("Enter what you are converting to: ").lower():
    case "megabyte"|"megabytes": print(f"{split[0]} {split[1]} = {int(split[0])/100:g} megabytes")
    case _: print("Invalid")