def sort(tver, value):
    
    start = 0
    end = len(tver) - 1

    while start <= end:
        
        mijin = (start + end) // 2

        
        if tver[mijin] == value:
            return mijin
        
        elif tver[mijin] < value:
            start = mijin + 1
        
        else:
            end = mijin - 1
    
    
    return -1


im_tver = [10, 11, 15, 23, 45, 70]
gtnelu_tver = 45


position_gtac = sort(im_tver, gtnelu_tver)

if position_gtac != -1:
    print(f"Found {gtnelu_tver} at position {position_gtac}")
else:
    print(f"{gtnelu_tver} listum chi")
