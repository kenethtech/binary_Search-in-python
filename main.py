#Recursive binary search

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)

    else:
        return -1

arr = []
ran = range(1,100)
for values in ran:
    arr.append(values)
x= int(input("Enter the number: "))

results = binary_search(arr, 0, len(arr)-1, x)

if results != -1:
    print("Number ", x)
    print("is present at index: ", str(results))

else:
    print("Sorry the number is not present!!")


