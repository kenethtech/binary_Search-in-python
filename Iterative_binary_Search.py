
def binary_search(arr, k):
    low = 0
    high = len(arr) - 1
    mid =0

    while low <= high:
        mid = (low + high)// 2

        if arr[mid] < k:
            low = mid + 1

        elif arr[mid] > k:
            high = mid-1

        else:
            return mid

    return -1
arr =[]
k = int(input("Enter the number: "))
ran = range(1,100)
for value in ran:
    arr.append(value)
result = binary_search(arr, k)
if result != -1:
    print("The number", k)
    print("is at index:", str(result))
else:
    print("Element is not present!!")
