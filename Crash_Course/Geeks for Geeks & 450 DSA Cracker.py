#                                     #### Array ####
#             #### Array Reverse ####
# def reverse(arr, right, left):
#     while left < right:
#         temp = arr[left]
#         arr[left] = arr[right]
#         arr[right] = temp
#         left += 1
#         right -= 1
#
#
# if __name__ == '__main__':
#     arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     reverse(arr, right=len(arr)-1, left=0)
#     print(arr)
#
#         #### Min and Max in Array ####
# def array(max, min):
#     print(f"The minimum value of this list is {min}, and thw maximum value is {max}")
#
# if __name__ == '__main__':
#     bye = [1, 5, 90, 700, 10, 7, 30]
#     array(max=max(bye), min=min(bye))
#

# def pyramids(height):
#     for i in range(1,height + 1):
#         spaces = ''* (height - i)
#         stars = '*'*(2*i-1)
#         print(spaces + stars)
# pyramids(10)

