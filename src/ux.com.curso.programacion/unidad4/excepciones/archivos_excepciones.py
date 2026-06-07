def abrir_archivo():
    try:
        with open("example.txt") as my_file:
            for line in my_file:
                print(line)
    except FileNotFoundError:
        print("The file example.txt was not found")
    except PermissionError:
        print("No permission to access the file example.txt")


def main():
    abrir_archivo()

if __name__ == "__main__":
    main()