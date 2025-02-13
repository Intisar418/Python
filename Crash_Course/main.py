# Write a program to read and print elements of an array.

n = int(input("Enter the number of elements: "))
array = []
for i in range(n):
    elements = int(input(f"Enter the element {i+1}: "))
    array.append(elements)

for i in array:
    print(i)


#Write a program to print all negative elements in an array.
def find_neg_nums(arr):
    for i in arr:
        if i < 0:
            print(i)


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, -2, -4, -6, -8]
    print("The negative elements of the array are: ")
    find_neg_nums(arr)

#Write a program to find the sum of all elements in an array
def sum_arr(lst):
    total = 0
    for i in lst:
        total += i

if __name__ == '__main__':
    result = sum_arr([1,2,3,4,5,6,7,8,9,10])
    print(result)



