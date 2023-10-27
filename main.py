def fibonacci_of(n):
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')

    if n in {0, 1}:
        return n

    p, fibonacci_number = 0, 1
    for _ in range(2, n + 1):
        p, fibonacci_number = fibonacci_number, p + fibonacci_number

    return fibonacci_number
