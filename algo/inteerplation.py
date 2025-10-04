def interpolat(s_list, value):
    
    if len(s_list) == 0:
        return -1
     
    low = 0
    high = len(s_list) - 1
    
    
    while low <= high and value >= s_list[low] and value <= s_list[high]:
        
        if low == high:
            if s_list[low] == value:
                return low
            return -1
        
        
        pos = low + ((value - s_list[low]) * (high - low)) // (s_list[high] - s_list[low])
        
        pos = max(low, min(pos, high))
        
        
        if s_list[pos] == value:
            return pos
        
        elif s_list[pos] < value:
            low = pos + 1
        
        else:
            high = pos - 1
    
    return -1


im_tver = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
gtnelu_tver = 60

position = interpolat(im_tver, gtnelu_tver)

if position != -1:
    print(f"Found {gtnelu_tver} at position {position}")
else:
    print(f"{gtnelu_tver} listum chka")


temp = [5, 12, 18, 25, 32, 41, 50, 63, 75, 88, 95]
gtnel_temp = 41

temp_position = interpolat(temperatures, gtnel_temp)

if temp_position != -1:
    print(f"Temperature {gtnel_temp}°F found at position {temp_position}")
else:
    print(f"Temperature {gtnel_temp}°F not recorded")
