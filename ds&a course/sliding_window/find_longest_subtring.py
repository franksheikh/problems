def find_longest_substring(s:str, k:int) -> int:
    counts = dict()
    count = 0
    max_count = 0
    
    l = 0
    for r in range(len(s)):
        char = s[r]
        counts[char] = counts.get(char,0) + 1
        count += 1
        while len(counts) > k:
            counts[s[l]] -= 1
            count -= 1
            if counts[s[l]] == 0:
                del counts[s[l]]
            l += 1
        max_count = max(count, max_count)
    
    return max_count
    
        
print(find_longest_substring('eceba',2))
            
        