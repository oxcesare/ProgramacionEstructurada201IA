"""
The song “99 Bottles of Beer” is a traditional song in the United States and Canada. It’s often sung by children on long trips, and it’s a great way to practice counting backwards. The song goes like this:
"""
def bottles_of_beer(n):
    for i in range(n, 0, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        if i > 1:
            print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.\n")
        else:
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print(f"Go to the store and buy some more, {n} bottles of beer on the wall.")

def main():
    bottles_of_beer(99)

if __name__ == "__main__":
    main()