import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()

    commands = []

    if command not in commands:
        print(f"{command}: command not found")
        sys.exit(1)


if __name__ == "__main__":
    main()
