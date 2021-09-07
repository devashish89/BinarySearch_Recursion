# Sorted List is primary condition for binary search
# Binary Search using Recursion

def binary_search_recursion(l, x, left, right):
    mid = (left + right) // 2
    if left > right:
        return -1
    elif x == l[mid]:
        return mid

    elif x < l[mid]:
        return binary_search_recursion(l, x, left, mid-1)

    else:
        return binary_search_recursion(l, x, mid+1, right)


def binary_search(l, x):
    return binary_search_recursion(l, x, 0, len(l) - 1)


if __name__ == '__main__':
    lst = [10, 20, 30, 18, 1, 43, 90, 56, 78]
    lst.sort()
    print("sorted list:", lst)
    print(binary_search(lst, 43))
