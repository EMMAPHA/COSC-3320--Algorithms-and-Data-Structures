import random
import math
import time

#Reverse Sorted array with input size n = 512
arr = [x for x in range(512,0,-1)]

def standard_quick_sort(arr):
    if len(arr) < 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]
        return standard_quick_sort(left) + [pivot] + standard_quick_sort(right)
    
#print(standard_quick_sort(arr))
    
def main():
    start_time = time.time()
    standard_quick_sort(arr)
     #time.sleep(1)
    end_time = time.time()
    print("{:0.6f}".format(end_time - start_time))

if __name__ == "__main__":
     main()   