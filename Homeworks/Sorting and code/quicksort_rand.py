import random
import math
import time

#Random array with input size n = 32
arr = [random.randint(0, 32) for x in range(32)]

def random_quick_sort(arr):
    if len(arr) < 1:
        return arr
    else:
        pivot = arr[random.randint(0, len(arr) - 1)]
        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]
        return random_quick_sort(left) + [pivot] + random_quick_sort(right)
    
#print(random_quick_sort(arr))
    
def main():
    start_time = time.time()
    random_quick_sort(arr)
    #time.sleep(1)
    end_time = time.time()
    print("{:0.6f}".format(end_time - start_time))

if __name__ == "__main__":
    main()