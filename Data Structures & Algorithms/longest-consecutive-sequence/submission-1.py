class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #sequence has start, middle end
            #end can have a lot of numbers before it
            #there are lots of middles
            #there is one start: identified if there is nothing 1 smaller before it
        
        longest = 0
        
        num_set = set(nums)

        for num in num_set:

            if num - 1 not in num_set:

                curr = num
                length = 1

                while curr + 1 in num_set:
                    length+=1
                    curr+=1

                longest = max(longest, length)


        return longest
                
        