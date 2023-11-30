def bubbleSort(x, n):
    if n == 1:
        return
    for i in range(n - 1):
        if x[i] > x[i + 1]:
            x[i], x[i + 1] = x[i + 1], x[i]
    bubbleSort(x, n - 1)

def binarySearch(arr, low, high, x):
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, high, x)
    else:
        return -1

c = int(input("Masukkan angka: "))
array = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
print("Sebelum sorting:", array)
bubbleSort(array, len(array))
print("Setelah sorting:", array)

result = binarySearch(array, 0, len(array) - 1, c)
if result != -1:
    print(f"Elemen ditemukan dalam indeks {result}.")
else:
    print("Elemen tidak valid dan tidak ditemukan pada list.")
