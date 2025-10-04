import math

def jump_search(arr, target):
    
    n = len(arr)
    step = int(math.sqrt(n)) 
    prev = 0

   
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1



numbers = [1, 3, 5, 7, 9, 13, 17, 19, 23, 29, 31]
target = 19

result = jump_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
