import sys

def prompt():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    command = input()
    return command

def get_commands():
    return {
        "exit": exit_cmd,
        "echo": echo_cmd,
        "type": type_cmd,
    }

def exit_cmd(num):
    code = num[0]
    # check if string is number
    if not code.isdigit():
        print(f"exit: {code}: numeric argument required")
        sys.exit(255)
    
    sys.exit(int(code))

def echo_cmd(args):
    msg = " ".join(args)
    print(msg)

def type_cmd(args):
    cmd = args[0]
    commands = get_commands()
    
    if cmd in commands:
        print(f"{cmd} is a shell builtin")
    else:
        print(f"{cmd} nonexistent")

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
