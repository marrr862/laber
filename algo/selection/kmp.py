def build_lps(pattern):
    
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    
    n = len(text)
    m = len(pattern)
    
    if m == 0:
        return []
    
    lps = build_lps(pattern)
    positions = []
    i = j = 0  
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            positions.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return positions


text = "ABABDABACDABABCABAB"
pattern = "ABABC"

result = kmp_search(text, pattern)
print(f"Text: {text}")
print(f"Pattern: {pattern}")
print(f"Found at positions: {result}")
