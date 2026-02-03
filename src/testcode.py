import time

def merge_sort(a_list):
    """Thuật toán sắp xếp trộn - Merge Sort"""
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_list = a_list[:mid]
        right_list = a_list[mid:]

        merge_sort(left_list)
        merge_sort(right_list)
        
        i, j, k = 0, 0, 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                a_list[k] = left_list[i]
                i += 1
            else:
                a_list[k] = right_list[j]
                j += 1
            k += 1
        while i < len(left_list):
            a_list[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            a_list[k] = right_list[j]
            j += 1
            k += 1



import random

def quick_sort(a_list):
    """Thuật toán Randomized Quick Sort"""
    quick_sort_helper(a_list, 0, len(a_list) - 1)

def quick_sort_helper(a_list, first, last):
    """Hàm đệ quy Quick Sort"""
    if first < last:
        split_point = partition(a_list, first, last)

        # Sắp xếp cho dãy các phần tử bên trái pivot
        quick_sort_helper(a_list, first, split_point - 1)

        # Sắp xếp cho dãy các phần tử bên phải pivot
        quick_sort_helper(a_list, split_point + 1, last)

def partition(a_list, first, last):
    """Hoare Partition với pivot ngẫu nhiên"""
    
    # Chọn pivot ngẫu nhiên và đưa về đầu mảng
    rand_pivot = random.randint(first, last)
    a_list[first], a_list[rand_pivot] = a_list[rand_pivot], a_list[first]

    pivot_value = a_list[first]     # Giá trị pivot chính là phần tử mảng có chỉ số ngẫu nhiên
    left_mark = first + 1           
    right_mark = last               

    while True:
        # Dịch con trỏ trái sang phải
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark += 1

        # Dịch con trỏ phải sang trái
        while right_mark >= left_mark and a_list[right_mark] >= pivot_value:
            right_mark -= 1

        # Nếu hai con trỏ vượt qua nhau thì dừng
        if right_mark < left_mark:
            break
        else:
            # Đổi chỗ hai phần tử sai phía
            a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]

    # Đặt pivot vào đúng vị trí
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

    # Trả về vị trí cuối cùng của pivot
    return right_mark



def heap_sort(a_list):
    """Thuật toán sắp xếp vun đống - Heap Sort"""
    heap_sort_helper(a_list, len(a_list))

def heap_sort_helper(a_list, n):
    """Hàm định nghĩa thêm cho heap_sort()"""
    
    # Build Max_Heap - Độ phức tạp O(log(n))
    for i in range(n // 2 - 1, -1, -1):
        heapify(a_list, n, i)
    
    # Heap Sort
    for i in range(n - 1, -1, -1):
        a_list[i], a_list[0] = a_list[0], a_list[i]
        heapify(a_list, i, 0)

def heapify(a_list, n, index):
    """Thao tác heapify tạo Max-Heap"""
    
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    
    if left < n and a_list[left] > a_list[largest]:
        largest = left

    if right < n and a_list[right] > a_list[largest]:
        largest = right
        
    if largest != index:
        a_list[largest], a_list[index] = a_list[index], a_list[largest]
        heapify(a_list, n, largest)


# Dữ liệu

T = 10

with open("gentest.txt", "r") as f:
    """Đọc dữ liệu testcase T từ file gentest.txt"""
    if T <= 5:
        for i, line in enumerate(f, 1):
            if i == T:
                arr_test = list(map(int, line.split()))
                break
    else:
        for i, line in enumerate(f, 1):
            if i == T:
                arr_test = list(map(float, line.split()))
                break


# Thuật toán

start = time.perf_counter()

# merge_sort(arr_test)

# quick_sort(arr_test)

# heap_sort(arr_test)

arr_test.sort()

# print(arr_test)

end = time.perf_counter()
print(f"Time: {end - start:.6f} seconds")