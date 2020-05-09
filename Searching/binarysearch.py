def binary_search(arr, low, high, number):

    while(low <= high):
        mid = (low + high)//2
        if arr[mid] == number:
            return True
        elif(arr[mid] > number):
            high = mid -1
        else:
            low = mid + 1
    return False
if __name__ == "__main__":
    print(binary_search([3,4,5,6,7,87,96534],0, 6, 87))



def binary_search_recursive(arr, low, high, number):
    if low <= high:
        mid = (low + high)//2
        if arr[mid] == number:
            return True
        if arr[mid] > number:
            return binary_search_recursive(arr, low, mid-1, number)
        return binary_search_recursive(arr, mid+1, high,  number)
    return False


if __name__ == "__main__":
    print(binary_search_recursive([3,4,5,6,7,87,96534],0, 6, 96534))

