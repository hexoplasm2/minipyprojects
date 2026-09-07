import os,sys

try:
    import msvcrt
    def getch():
        return msvcrt.getch().decode("utf-8", errors="ignore")
except ImportError:
    import tty,termios

    def getch():
        fd = sys.stdin.fileno()
        tsettings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, tsettings)
        return ch

def getKey():
    ch = getch()

    if ch in ("\x00", "\xe0"):
        ch2 = getch()
        if ch2 == "H": return "up"
        if ch2 == "P": return "down"
        
    elif ch == "\x1b":
        ch2 = getch()
        if ch2 == "[":
            ch3 = getch()
            if ch3 == "A": return "up"
            if ch3 == "B": return "down"
            
    if ch in ("\r","\n"):
        return "enter"
    
    return ch





def multiChoice(*options):
    selected = 0

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        for k,v in enumerate(options):
            if k == selected:
                print(f"> {v}")
            else:
                print(f"  {v}")
        
        key = getKey()
        
        if key == "up" and selected > 0:
            selected -= 1
        elif key == "down" and selected < len(options) - 1:
            selected += 1
        elif key == "enter":
            os.system("cls" if os.name == "nt" else "clear")
            return selected, options[selected]
        elif key == "q":
            return None, None



def main():
    chosen = multiChoice("First", "Second", "Third")
    print(f"\nYou selected: Index {chosen[0]} or {chosen[1]}")

if __name__ == "__main__":
    main()