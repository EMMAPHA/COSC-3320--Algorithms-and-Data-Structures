import random
import math
import time


#arr = [random.randint(0, 64) for x in range(64)]
#arr = [x for x in range(32,0,-1)]

# Example: Odd-Even for input size n = 32
arr = [x for x in range(32) if x % 2 != 0] + [x for x in range(32) if x % 2 == 0]

def merged(left, right):
    merged_array = []
    m, n = len(left), len(right)
    i, j = 0, 0
    while i < m and j < n:
        if left[i] <= right[j]:
            
            merged_array.append(left[i])
            i += 1
        else:
            merged_array.append(right[j])
            j += 1
    if i == m:  # merged all elements from left
        merged_array.extend(left[j:n])
    else:  # merged all elements from right
        merged_array.extend(right[i:m])
    return merged_array

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        mid = n // 2  # integer division
        left, right = arr[0:mid], arr[mid:n]
        sorted_left, sorted_right = merge_sort(left), merge_sort(right)
        return merged(sorted_left, sorted_right)
# print(arr) 

def main():
     start_time = time.time()
     merge_sort(arr)
     #time.sleep(1)
     end_time = time.time()
     print("{:0.6f}".format(end_time - start_time))

if __name__ == "__main__":
     main()