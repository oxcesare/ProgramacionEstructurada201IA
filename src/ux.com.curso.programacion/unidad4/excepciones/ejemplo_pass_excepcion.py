def read_small_integer():
    while True:
        try:
            input_str = input("Please type in an integer: ")
            number = int(input_str)
            if number < 100:
                return number
        except ValueError:
            pass # this command doesn't actually do anything

        print("This input is invalid")

number = read_small_integer()
print(number, "to the power of three is", number**3)


def main():
    number = read_small_integer()
    print(number, "to the power of three is", number**3)
    
if __name__ == "__main__":
    main()