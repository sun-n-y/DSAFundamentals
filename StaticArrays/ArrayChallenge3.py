

# for i in range(len(myArray)):
#     print(myArray[i])
#
# i = 0
# while i < len(myArray):
#     print(myArray[i])
#     i += 1

# def removeEnd(arr, length):
#     if length > 0:
#         arr[length - 1] = 0
#
# removeEnd(myArray, len(myArray))
# print(myArray)
#
# def removeMiddle(arr, i, length):
#     for index in range(i + 1, length):
#         arr[index - 1] = arr[index]
#
# removeMiddle(myArray, 9, len(myArray))
# print(myArray)

# def insertEnd(arr, n, length, capacity):
#     if length < capacity:
#         arr[length - 1] = n
#
# insertEnd(myArray, 101, len(myArray), 12)
# print(myArray)

# def insertMiddle(arr, n, i, length):
#     for index in range(length - 1, i - 1, -1):
#         arr[index] = arr[index - 1]
#
#     arr[i] = n
#
# insertMiddle(myArray, 101, 1, len(myArray))
# print(myArray)

myArray = [0, 1, 1, 1, 2, 3, 3, 3, 4, 6, 6]

def removeDuplicates(arr, length):
    l = 1

    for r in range(1, length):
        if arr[r - 1] != arr[r]:
            arr[l] = arr[r]
            l += 1

removeDuplicates(myArray, len(myArray))
print(myArray)






