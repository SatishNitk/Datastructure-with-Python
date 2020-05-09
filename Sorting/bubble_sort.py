def bubble(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]
    print(arr)

if __name__ == '__main__':
    bubble([32,43,54,54,45,3,2,4,1,56, 9])  