# init an array
myArray = [1, 2, 3]

# access element
print(myArray[0])

# traverse through an array
# range returns a sequence of numbers starting 0 and increment by 1 by default
# and stops before the given number.
for i in range(len(myArray)):
    print(myArray[i])

print(len(myArray))

# or

i = 0
while i < len(myArray):
    print(myArray[i])
    i += 1


# deleting from end array

def removeEnd(arr, length):
    if length > 0:
        arr[length - 1] = 0
    else:
        return print('array length is 0')

#removeEnd(myArray,len(myArray))
#print(myArray)


# deleting from ith index, shifting elements to left
def removeMiddle(arr, i, length):
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]

removeMiddle(myArray, 0, len(myArray))
print(myArray)