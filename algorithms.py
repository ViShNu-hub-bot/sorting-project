# algorithms.py
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def inorder_traversal(root):
    result = []
    if root:
        result += inorder_traversal(root.left)
        result.append(root.val)
        result += inorder_traversal(root.right)
    return result

class HashTable:
    pass

class UnionFind:
    pass
