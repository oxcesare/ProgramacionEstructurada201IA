def factorial(n):
    if n < 0:
        raise ValueError("The input was negative: " + str(n))
    k = 1
    for i in range(2, n + 1):
        k *= i
    return k

def main():
  try:
    print(factorial(-5))
    print(factorial(-2))
    print(factorial(-10))
  except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
    main()