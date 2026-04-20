""""
    Write a function called triangle that takes a string and an 
    integer and draws a pyramid with the given height, made up using copies of the string. Here’s an example of a pyramid with 5 levels, using the string 'L'.
"""

def triangle(text, height):
    for i in range(1, height + 1):
        print(text * i)

def main():
    triangle("L", 10)

if __name__ == "__main__":
    main()