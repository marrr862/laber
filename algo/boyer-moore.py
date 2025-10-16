def boyer (text,lenn):
    if not lenn or not text:
        return []
    
  
    bad_char_table = bad_char(lenn)
    good_suffix_table = good_suffix(lenn)
    
    matches = []
    n, m = len(text), len(lenn)
    i = 0  
    
    while i <= n - m:
        j = m - 1
        while j >= 0 and lenn[j] == text[i + j]:
            j -= 1
        
        if j < 0:
            
            matches.append(i)
            if i + m < n:
                shift = good_suffix_table[0]
                i += shift
            else:
                i += 1
        else:
            
            bad_char_shift = bad_char_table.get(text[i + j], m)
            good_suffix_shift = good_suffix_table[j + 1]
            
            
            shift = max(1, bad_char_shift - (m - 1 - j), good_suffix_shift)
            i += shift
    
    return matches


def bad_char(lenn):
    
    table = {}
    m = len(lenn)
    
    for i in range(m - 1): 
        char = lenn[i]
        table[char] = m - 1 - i
    
    return table


def good_suffix(lenn):
   
    m = len(lenn)
    table = [0] * (m + 1)
    
    
    i, j = m, m + 1
    border_pos = [0] * (m + 1)
    border_pos[i] = j
    
    while i > 0:
        while j <= m and lenn[i - 1] != lenn[j - 1]:
            if table[j] == 0:
                table[j] = j - i
            j = border_pos[j]
        i -= 1
        j -= 1
        border_pos[i] = j
    
    j = border_pos[0]
    for i in range(m + 1):
        if table[i] == 0:
            table[i] = j
        if i == j:
            j = border_pos[j]
    
    return table



if __name__ == "__main__":
     
    text = "ABAAABCDABCABCABABC"
    lenn = "ABC"
    print(f"Searching for '{lenn}' in '{text}'")
    results = boyer (text, lenn)
    print(f"Found at positions: {results}")
    print()
    
    
    text = "Hello World"
    lenn = "Python"
    print(f"Searching for '{lenn}' in '{text}'")
    results = boyer (text, lenn)
    print(f"Found at positions: {results}")
    print()
    
    
    text = "banana"
    lenn = "ana"
    print(f"Searching for '{lenn}' in '{text}'")
    results = boyer (text, lenn)
    print(f"Found at positions: {results}")
