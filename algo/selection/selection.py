def selection_s(tver):
    
    
    arr = tver.copy()
    n = len(arr)
    
    for i in range(n):
        
        min_index = i
        
        
        for j in range(i + 1, n):
            
            if arr[j] < arr[min_index]:
                min_index = j
        
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


im_tver = [64, 25, 12, 22, 11]
print("Orig list:", im_tver)

s_tver = selection_s(im_tver)
print("Sorted list:  ", s_tver)
