"""
    Write a function named print_right that takes a string named text as a parameter and prints 
    the string with enough leading spaces that the 
    last letter of the string is in the 40th column of the display.
"""
def print_right(text):
    spaces = 40 - len(text)
    print(" " * spaces + text)

def main():
    print_right("Hello, World!")

if __name__ == "__main__":
    main()