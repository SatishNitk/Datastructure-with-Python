def linear_search(arr, n):
    return  True if [True for i in range(len(arr)) if arr[i] == n] else False

if __name__ == '__main__':
    print(linear_search([12,22,33,43,54,43], 12))