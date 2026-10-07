import os,sys
from rich.console import Console
from rich.live import Live

console = Console(highlight=False)

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



def clear():
    os.system("cls" if os.name == "nt" else "clear")



def multiChoice(*options):
    clear()
    selected = 0

    def render():
        menu_text = []
        for k,v in enumerate(options):
            if k == selected:
                menu_text.append(f"[yellow]>[/] [white bold]{v}[/]")
            else:
                menu_text.append(f"  [white]{v}[/]")
        return "\n".join(menu_text)

    with Live(render(), console=console, auto_refresh=False) as live:
        while True:
            key = getKey()
            
            if key == "up" and selected > 0:
                selected -= 1
            elif key == "down" and selected < len(options) - 1:
                selected += 1
            elif key == "enter":
                clear()
                return selected, options[selected]
            elif key == "q":
                return None, None
            live.update(render(), refresh=True)
    console.clear()

    try:
        import termios
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
    except ImportError:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()

    return selected, options[selected]

def main():
    chosen = multiChoice("First", "Second", "Third")
    print(f"\nYou selected: Index {chosen[0]} or {chosen[1]}")

if __name__ == "__main__":
    main()