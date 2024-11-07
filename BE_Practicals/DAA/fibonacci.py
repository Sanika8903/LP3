# Write a program non-recursive and recursive program to calculate Fibonacci numbers and
# analyze their time and space complexity.


# Non-Recursive Fibonacci Function
def fibonacci_non_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        fib = a + b
        a = b
        b = fib
    return b

# Recursive Fibonacci Function
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Take input from the user
n = int(input("Enter the number of terms for Fibonacci: "))

# Output
print(f"Fibonacci for {n}th term (non-recursive):", fibonacci_non_recursive(n))
print(f"Fibonacci for {n}th term (recursive):", fibonacci_recursive(n))
