import sys

def prompt():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    command = input()
    return command

def main():
    # Wait for user input
    commands = []
    command = prompt()

    while command:
        if command not in commands:
            print(f"{command}: command not found")
        command = prompt() 

if __name__ == "__main__":
    main()
