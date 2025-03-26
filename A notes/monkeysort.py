import random
import time

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def monkey_sort(arr):
    attempts = 0

    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
        print(f"Attempt {attempts}: {arr} - throwing shit on wall and praying...")
        

    print(f"\nAfter {attempts} attempts, monkey successfully achieved consciousness and sorted the list:")
    print(arr)

if __name__ == "__main__":
    # Example usage
    unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    
    print("Original list:")
    print(unsorted_list)

    print("\nMonkey sorting!\n")
    monkey_sort(unsorted_list)
