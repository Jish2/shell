import sys

def prompt():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    command = input()
    return command

def get_commands():
    return {
        "exit": exit   
    }

def exit(num):
    code = num[0]
    # check if string is number
    if not code.isdigit():
        print(f"exit: {code}: numeric argument required")
        sys.exit(255)
    
    sys.exit(int(code))

def main():
    # Wait for user input
    commands = get_commands()
    command = prompt()

    while command:
        args = command.split(" ")
        if args[0] not in commands:
            print(f"{args[0]}: command not found")
        else:
            commands[args[0]](args[1:])
        command = prompt() 

if __name__ == "__main__":
    main()
