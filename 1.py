def is_even(num: int) -> bool:
    return num & 1 != 1

if __name__ == "__main__":
    print(is_even(2))
    print(is_even(1))
    print(is_even(0))
    print(is_even(-1))
    print(is_even(-2))
