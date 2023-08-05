from virtual_shell import VirtualShell

def main():
    shell = VirtualShell()
    while True:
        command = input(f"{shell.current_directory.name}> ")
        tokens = command.split()

        if tokens[0] == "ls":
            print(shell.list_directory())
        elif tokens[0] == "cd":
            shell.change_directory(tokens[1])
        elif tokens[0] == "mkdir":
            shell.make_directory(tokens[1])
        elif tokens[0] == "touch":
            shell.create_file(tokens[1])
        elif tokens[0] == "exit":
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
