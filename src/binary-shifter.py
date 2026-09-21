inp = input("Enter a binary number: ")
try:
    pro = int(inp,2)
    shift = int(input("How many places do you want to shift: "))
    match input("Right [0] or Left [1] shift: "):
        case "0":print(f"{bin(pro>>shift)} = {pro>>shift}")
        case "1":print(f"{bin(pro<<shift)} = {pro<<shift}")
        case  _ :print("Invalid.")
except:print("Error!")