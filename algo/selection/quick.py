def quick_s(arr):
    
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]  
    left = [x for x in arr[1:] if x <= pivot]   
    right = [x for x in arr[1:] if x > pivot]   
    
    return quick_s(left) + [pivot] + quick_s(right)


tver = [64, 34, 25, 12, 22, 11, 90]
print("Orig:", tver)
print("Sorted:  ", quick_s(tver))
