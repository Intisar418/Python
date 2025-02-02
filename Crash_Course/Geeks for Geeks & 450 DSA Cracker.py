                                         #### Array Reverse ####

def reverse(arr, right, left):
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    reverse(arr, right=len(arr)-1, left=0)
    print(arr)
