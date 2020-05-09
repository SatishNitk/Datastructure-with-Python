
def partition_index_from_arr(arr, low, high):
    while low < high:
        mid = (low + high) // 2
        if low == high:
            return low
        elif mid < high  and arr[mid] > arr[mid+1]:
            return mid
        elif mid > low and arr[mid] < arr[mid-1]:
            return mid -1
        elif(arr[mid] < arr[low]):
            high = mid + 1
        else:
            low  = mid + 1
    return -1

def binary_searchUtil(arr, low, high, number):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == number:
            return True
        elif(arr[mid] > number):
            return binary_searchUtil(arr, low, mid-1, number)
        return binary_searchUtil(arr, mid+1, high, number)
    return False

    

def binary_search(arr, low, high, number):
    if low <= high:
        partition_index = partition_index_from_arr(arr, low, high)
        print(partition_index)

        if partition_index == -1:
            return binary_searchUtil(arr, low, high, number)
        if arr[partition_index] == number:
            return True
        if arr[0] <= number:
            return binary_searchUtil(arr, low, partition_index-1, number)
        else:
            return binary_searchUtil(arr, partition_index + 1, high, number)


if __name__ == '__main__':
    print(binary_search([4,5,1,2,3], 0, 4, 4))