def selection(arr):
    i=0
    k =0
    for i in range(0, len(arr) -1):
        curr_small = arr[i]
        k =i
        for j in range(i+1, len(arr)):
            if curr_small > arr[j]:
                curr_small = arr[j]
                k = j
        arr[i], arr[k] = arr[k], arr[i]
    return arr

if __name__ == '__main__':
    print(selection([1,43,34,4,3,2,5, 1]))