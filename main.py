def main():
    print("Hello from demo!")


def my_add(a: int, b: int) -> int:
    return a + b


def my_subtract(a: int, b: int) -> int:
    return a - b


if __name__ == "__main__":
    main()
    my_add(1, 2)
    my_subtract(5, 3)
