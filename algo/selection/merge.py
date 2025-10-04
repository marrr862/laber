def merge_s(tver):
    
    
    if len(tver) <= 1:
        return tver
    
    
    mejtex = len(tver) // 2
    left_half = tver[:mejtex]    
    right_half = tver[mejtex:]   
    
    
    left_s = merge_s(left_half)
    right_s = merge_s(right_half)
    
    
    return merge(left_s, right_s)

def merge(left, right):
    
    result = []
    i = j = 0  
    
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
   
    while i < len(left):
        result.append(left[i])
        i += 1
    
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result


im_tver = [38, 27, 43, 3, 9, 82, 10]
print("Orig list:", im_tver)

s_tver = merge_s(im_tver)s
print("Sorted list:  ", s_tver)







































