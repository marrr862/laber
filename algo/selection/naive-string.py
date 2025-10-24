def naive_string_match(text, pattern):  
    n = len(text)
    m = len(pattern)
    positions = []   
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if text[i + j] != pattern[j]:
                break
            j += 1        
        if j == m:
            positions.append(i)    
    return positions




text = "ABABDABACDABABCABAB"
pattern = "ABABC"

print(f"Text: {text}")
print(f"Pattern: {pattern}")

matches = naive_string_match(text, pattern)

if matches:
    print(f"Pattern found at positions: {matches}")
else:
    print("Pattern not found in text")

