
def fibonacci_series(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
n = int(input("Enter the number of terms: "))
fib_series = fibonacci_series(n)
print(f"The first {n} terms of the Fibonacci series are: {fib_series}")
