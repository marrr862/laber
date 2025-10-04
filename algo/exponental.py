def exponen(s_list, value):
    
    if len(s_list) == 0:
        return -1
    
    if s_list[0] == value:
        return 0
    
    
    index = 1
    while index < len(s_list) and s_list[index] <= value:
        index = index * 2
    
    
    low = index // 2
    high = min(index, len(s_list) - 1)
    
    while low <= high:
        mid = (low + high) // 2
        
        if s_list[mid] == value:
            return mid
        elif s_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1


im_tver = [2, 5, 7, 10, 14, 18, 21, 30, 35, 40, 45, 50]
gtnelu_tver = 18

position = exponen(im_tver, gtnelu_tver)

if position != -1:
    print(f"Found {gtnelu_tver} at position {position}")
else:
    print(f"{gtnelu_tver} listum chka")
