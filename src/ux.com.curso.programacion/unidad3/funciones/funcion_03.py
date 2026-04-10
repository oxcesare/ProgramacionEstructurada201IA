# Variables y parametros locales

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

def print_twice(string):
    print(string)
    print(string)

def main():
    line1 = 'Always look on the '
    line2 = 'bright side of life.'
    cat_twice(line1, line2)

if __name__ == "__main__":
    main()