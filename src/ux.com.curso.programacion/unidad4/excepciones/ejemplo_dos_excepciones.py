def read_integer():
    while True:
        try:
            input_str = input("Please type in an integer: ")
            return int(input_str)
        except ValueError:
            print("This input is invalid")

number = read_integer()
print("Thank you!")
print(number, "to the power of three is", number**3)


def main():
    number = read_integer()
    print("Thank you!")
    print(number, "to the power of three is", number**3)

if __name__ == "__main__":
    main()