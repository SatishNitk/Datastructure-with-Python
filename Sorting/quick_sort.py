def partition(arr, l, r):
    pivot = arr[r]
    j = (l - 1)
    for i in range(l, r):
        if arr[i] < pivot:
            j = j + 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[j+1], arr[r] = arr[r], arr[j+1]
    return j+1


def quick_sort(arr, l, r):
    if l < r:
        partition_index = partition(arr,l, r)
        quick_sort(arr, l, partition_index - 1)
        quick_sort(arr, partition_index + 1, r)


if __name__ == "__main__":
    arr  = [2,4,1,5,3]
    quick_sort(arr ,0,len(arr) - 1)
    print(arr)