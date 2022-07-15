from typing import Iterable, List


def sort(arr: List[Iterable]) -> None:
    arr.sort()
#   return sorted(arr)


if __name__ == "__main__":
    print(sort([1,2,3,1]))
    a = [1,2,3,2,1]
    sort(a)
    print(a)