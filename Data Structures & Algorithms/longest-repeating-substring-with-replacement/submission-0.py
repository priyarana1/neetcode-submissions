class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        longest = 0


        for r in range(len(s)):

            freq = {}

            for c in s[l:r+1]:
                freq[c] = freq.get(c, 0) + 1
            
            max_freq = 0
            for val in freq.values():
                max_freq = max(max_freq, val)

            chars_to_replace = (r - l + 1) - max_freq


            if k < chars_to_replace:
                l = l + 1

            longest = max(longest, r - l + 1)

            

        
        return longest
                

