def insertion_sort(arr):
    mylist = arr.copy()
    n = len(mylist)
    
    for i in range(1, n):
        insert_index = i
        current_value = mylist[i]
        
        for j in range(i-1, -1, -1):
            if mylist[j] > current_value:
                mylist[j+1] = mylist[j]
                insert_index = j
            else:
                break
        
    mylist[insert_index] = current_value
    
    return mylist

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i + 1


def quick_sort(arr):
    data = arr.copy()  

    def quicksort(array, low=0, high=None):
        if high is None:
            high = len(array) - 1

        if low < high:
            pivot_index = partition(array, low, high)
            quicksort(array, low, pivot_index - 1)
            quicksort(array, pivot_index + 1, high)

    quicksort(data)
    return data

def counting_sort(arr):
  max_val = max(arr)
  count = [0] * (max_val + 1)

  while len(arr) > 0:
    num = arr.pop(0)
    count[num] += 1

  for i in range(len(count)):
    while count[i] > 0:
      arr.append(i)
      count[i] -= 1

  return arr

while True:
    try:
        n = int(input("Masukkan jumlah elemen: "))
        if n <= 0:
            print("Jumlah harus lebih dari 0")
        else:
            break
    except:
        print("Input harus bilangan bulat non-negatif")


arr = []
for i in range(n):
    while True:
        try:
            x = int(input(f"Masukkan elemen ke-{i+1}: "))
            if x < 0:
                print("Hanya boleh bilangan non-negatif!")
            else:
                arr.append(x)
                break
        except:
            print("Input tidak valid! Harus bilangan bulat.")



print("\nArray awal: ", arr)

print("\nInsertion Sort: ", insertion_sort(arr))

print("\nQuick Sort: ", quick_sort(arr))
print()
print("Counting Sort: ", counting_sort(arr))