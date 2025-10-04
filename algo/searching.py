def gtnel_index(tver, value):
    
    for position in range(len(tver)):
        
        if tver[position] == value:
            return position
    
    return -1


im_tver = [10, 23, 45, 70, 11, 15]
gtnelu_tver= 70


position_found = gtnel_index(im_tver, gtnelu_tver)

if position_found != -1:
    print(f"Found {gtnelu_tver} at position {position_found}")
else:
    print(f"{gtnelu_tver} listum chi")
