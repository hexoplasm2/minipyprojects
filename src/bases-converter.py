print("This converts characters on your keyboard to a decimal number or a decimal number to a character while following the ASCII system.")
input("Press Enter to continue: ")
inp = input("Enter a character(A)/decimal(65)/hexadecimal(0x41)/binary(0b1000001) number: ")

while True:
    try:
        x = int(inp,0)
        y = int(inp,16)
        z = int(inp)

        if inp.lower().startswith("0x"):
            match input("Convert hexadecimal to character[0], decimal[1] or binary[2]: "):
                case "0": print(f"{inp} = {chr(x)}")
                case "1": print(f"{inp} = {y}")
                case "2": print(f"{inp} = {bin(y)}")
        elif inp.lower().startswith("0b"):
            match input("Convert binary to character[0], decimal[1] or hexadecimal[2]: "):
                case "0": print(f"{inp} = {chr(x)}")
                case "1": print(f"{inp} = {int(inp,2)}")
                case "2": print(f"{inp} = {hex(x)}")
        else:
            match input("Convert decimal to character[0], binary[1] or hexadecimal[2]: "):
                case "0": print(f"{inp} = {chr(z)}")
                case "1": print(f"{inp} = {bin(z)}")
                case "2": print(f"{inp} = {hex(z)}")
    except ValueError:
        x = ord(inp)

        match input("Convert character to decimal[0], binary[1] or hexadecimal[2]: "):
            case "0": print(f"{inp} = {x}")
            case "1": print(f"{inp} = {bin(x)}")
            case "2": print(f"{inp} = {hex(x)}")