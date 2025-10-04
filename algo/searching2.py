def search_errordov(s_list,value):
    
    low = 0
    high = len(s_list) - 1

   
    while low <= high:
        
        third = (high - low) // 3
        mid1 = low + third
        mid2 = high - third

       
        if s_list[mid1] == value:
            return mid1
        if s_list[mid2] == value:
            return mid2

        
        if value < s_list[mid1]:
           
            high = mid1 - 1
        elif value > s_list[mid2]:
           
            low = mid2 + 1
        else:
            
            low = mid1 + 1
            high = mid2 - 1

   
    return -1


im_tver = [2, 5, 7, 10, 14, 18, 21, 30]
gtnelu_tver = 18


position_found = search_errordov(im_tver, gtnelu_tver)

if position_found != -1:
    print(f"Found {gtnelu_tver} at position {position_found}")
else:
    print(f"{gtnelu_tver} listum chka")
