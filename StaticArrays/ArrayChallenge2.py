# initialize an array
# traverse through an array, for and while loop
# delete from end of array
# remove ith index in array, then shift elements to left
# insertion at end of array, assuming there is open position
# insert n into index ith after shifting elements to the right, [4, 5, 0]
# remove duplicates from sorted array and return num of unique values
# remove element in place and shift to left [0,0,1,1,2,3,1], remove 1s

myArray = [1, 2, 2, 3, 3, 4, 4, 5]
#
# for i in range(len(myArray)):
#     print(myArray[i])
#
# i = 0
# while i < len(myArray):
#     print(myArray[i])
#     i += 1
#
# def removeEnd(arr, length):
#     if length > 0:
#         arr[length - 1] = 0
#
# removeEnd(myArray,len(myArray))
# print(myArray)

# def removeMiddle(arr, i, length):
#     arr[i] = 0
#     for index in range(i + 1, length):
#         arr[index - 1] = arr[index]
#
# removeMiddle(myArray, 1, len(myArray))
# print(myArray)

# def insertEnd(arr, n, length, capacity):
#     if length < capacity:
#         arr[length] = n
#
# insertEnd(myArray, 77, len(myArray), (len(myArray) + 1))
# print(myArray)

# array2 = [11, 23, 45, 67, 0]
#
# def insertMiddle(arr, i, n, length):
#     for index in range(length - 1, i - 1, -1):
#         arr[index] = arr[index - 1]
#     arr[i] = n
#
# insertMiddle(array2, 0, 555, len(array2))
# print(array2)

# myArray = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#
# def removeDuplicates(arr, length):
#     l = 1
#
#     for r in range(1, length):
#         if arr[r] != arr[r - 1]:
#             arr[l] = arr[r]
#             l += 1
#     return l
#
#
# removeDuplicates(myArray, len(myArray))
# print(myArray)
#
array3 =[1, 2, 3]

for index in range(len(array3)):
    print(index)

print(len(array3))
