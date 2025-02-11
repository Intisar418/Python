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

















