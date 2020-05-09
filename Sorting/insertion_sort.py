def insertion(arr):
    for i in range(0, len(arr) -1):
        for j in range(i+1, 0 , -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    print(arr)

if __name__ == "__main__":
    insertion([3,2,1,4,45, 8])

