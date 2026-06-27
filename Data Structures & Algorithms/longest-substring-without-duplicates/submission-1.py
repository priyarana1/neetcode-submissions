class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = {}
        longest = 0

        l = 0 #left pointer starts at beginning

        for r in range(len(s)): #right pointer will keep iterating

            char = s[r] 

            if char in seen and seen[char] >= l: #if the current carr is seen and that instance is in the current window

                l = seen[char] + 1 #move the left pointer to the char after the repeated number
                seen[char] = r #update that character to have the latest index it was seen at

            
            longest = max(longest, r - l + 1)
            seen[char] = r
        
        return longest





