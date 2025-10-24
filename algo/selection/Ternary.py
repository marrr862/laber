def ternary(arr, target):
    left = 0
    right = len(arr) - 1
    
    print(f"Searching for {target} in array: {arr}")
    print()
    
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        print(f"Search range: [{left}, {right}]")
        print(f"Mid points: mid1={mid1}(value={arr[mid1]}), mid2={mid2}(value={arr[mid2]})")
        
        if arr[mid1] == target:
            print(f" Found at mid1 position {mid1}!")
            return mid1
        
        if arr[mid2] == target:
            print(f" Found at mid2 position {mid2}!")
            return mid2
        
        if target < arr[mid1]:
            print(f"Target {target} < {arr[mid1]}, searching left segment [{left}, {mid1-1}]")
            right = mid1 - 1
        elif target > arr[mid2]:
            print(f"Target {target} > {arr[mid2]}, searching right segment [{mid2+1}, {right}]")
            left = mid2 + 1
        else:
            print(f"{arr[mid1]} < Target {target} < {arr[mid2]}, searching middle segment [{mid1+1}, {mid2-1}]")
            left = mid1 + 1
            right = mid2 - 1
        
        print()
    
    print(f"Target {target} not found")
    return -1

def orinak():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    target = 7
    
    print("Ternary Search")
    print("=" * 50)
    result = ternary(arr, target)
    print(f"\nFinal result: Index {result}")

# Run the example
orinak()
