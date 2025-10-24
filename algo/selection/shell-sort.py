def shell_s(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  
    return arr


tver = [64, 34, 25, 12, 22, 11, 90, 5]
print("Orig zangvac:", tver)
s_tver = shell_s(tver.copy())
print("Dasavorvac zangvac:", s_tver)
