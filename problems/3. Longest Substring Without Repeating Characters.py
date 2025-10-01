'''
abcabcbbc
 l
   r

use set to keep track of duplicates
iterate through string
    while r_char == a character already in the set
            remove the left_character from our set until it equals r_char
            increment our left
    set max answer = max(ans, r - l + 1)
    add right character to our set

return max ans

    
longest/shortest substring/subarray with property X" is a classic sliding window giveaway
Other keywords include:
    - "Maximum/minimum length"
    - "Contiguous subarray/substring"
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        seen = set()
        
        for r in range(len(s)):
            r_char = s[r]

            while r_char in seen:
                seen.remove(s[l])
                l += 1
            ans = max(ans, r - l + 1)
            seen.add(r_char)
        return ans



        