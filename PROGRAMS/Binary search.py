
def binary_search(arr, first, last, x):


	if last >= first:

		mid = ((last + first) // 2) - 1
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, first, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, last, x)

	else:
		return -1

arr = [ 'ish',
        'saugat',
        'hamza',
        'Moeez' ]


x =  'ish'

result = binary_search(arr, 0, len(arr), x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
