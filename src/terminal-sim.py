import os
import sys





print("Welcome to the terminal")
username = input("Enter a username: ")
desktop_username = input("Enter a desktop username: ")
command_prefix = username+"@"+desktop_username+":"+os.getcwd()+"$ "


while True:
    current_command = input(command_prefix)
    if current_command.startswith("mkdir"):
        processing = current_command.removeprefix("mkdir ")
        os.mkdir(processing)
    if current_command.startswith("cd"):
        processing = current_command.removeprefix("cd ")
        os.chdir(processing)
    if current_command.startswith("ls"):
        for i in os.listdir(os.getcwd()):
            print(i)
    if current_command.startswith("cat"):
        try:
            filename = current_command.split(" ", 1)[1]
        except IndexError:
            print("Usage: cat <filename>")
        else:
            try:
                with open(filename, 'r') as f:
                    content = f.read()
                    print(content)
            except FileNotFoundError:
                print(f"Error: File '{filename}' not found.")
            except IOError as e:
                print(f"Error reading file: {e}")
    if current_command.startswith("touch"):
        try:
            filename = current_command.split(" ", 1)[1]
        except IndexError:
            print("Usage: touch <filename>")
        else:
            content = str(input(f"Enter content for '{filename}': "))
            try:
                with open(filename, "w") as command:
                    command.write(content)
                print(f"Successfully created and wrote to '{filename}'.")
            except IOError as e:
                print(f"Error: Could not write to file '{filename}'. Details: {e}")
    command_prefix = username+"@"+desktop_username+":"+os.getcwd()+"$ "