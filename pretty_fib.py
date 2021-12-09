def fibonacci(seq_len: int = 10) -> int:
    """This is Fibonacci sequence generator.

    Args:
        seq_len (int, optional): desired Fibonacci sequence lenght. Defaults to 10.

    Yields:
        int: Fibonacci next element
    """
    a, b = 0, 1
    for _ in range(seq_len):
        yield a
        a, b = b, b + a


if __name__ == "__main__":
    print("Fibonacci sequence, pretty version")
    for elem in fibonacci(13):
        print(elem)