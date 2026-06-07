def obtener_edad():
   try:
    age = int(input("Please type in your age: "))
   except ValueError:
    age = -1

    if age >= 0 and age <= 150:
        print("That is a fine age")
    else:
        print("This is not a valid age")

def main():
    obtener_edad()

if __name__ == "__main__":
    main()
