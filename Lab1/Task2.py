array1 = [1, 2, 5, 6, 3, 4,]
array2 = [1, 2, 3, 4, 5, 6,]

def list(arr):
    var = "True"
    for i in range(1, len(arr)):
        if (arr[i - 1] > arr[i]):
            var = 'False'
            break
    return var

print(list(array1))
print(list(array2))