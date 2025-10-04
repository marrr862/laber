def bubble_s(tver):
    
    
    arr = tver.copy()
    n = len(arr)
    
    
    for i in range(n):
        
        swapped = False
        
        
        for j in range(0, n - i - 1):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
       
        if not swapped:
            break
    
    return arr


im_tver = [64, 34, 25, 12, 22, 11, 90]
print("Orig list:", im_tver)

s_tver = bubble_s(im_tver)
print("Sorted list:  ", s_tver)
