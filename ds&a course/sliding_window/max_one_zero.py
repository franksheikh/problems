# SLIDING WINDOW
# Time complexity -> O(n) -> Amortized
# Space complexity -> O(1)
def find_length_max_zeros(s):
    l = 0
    ans = 0
    o_count = 0
    for r in range(len(s)):
        if s[r] == '0':
            o_count += 1
        while o_count > 1:
            if s[l] == '0':
                o_count -= 1
            l += 1        
        ans = max(ans, r - l + 1)
    return ans
