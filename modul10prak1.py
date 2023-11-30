def bubbleSort(x):
    n = len(x)
    for i in range(n):
        for j in range(0, n-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]

def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

c = int(input("Masukkan angka: "))
array = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
bubbleSort(array)
print("Setelah before:", array)

result = binarySearch(array, c)
if result != -1:
    print(f"Elemen ditemukan dalam indeks {result}.")
else:
    print("Elemen tidak valid dan tidak ditemukan pada list.")