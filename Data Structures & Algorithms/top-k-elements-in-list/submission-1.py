class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    #iterate through list and create frequency map
        freq_map = {}
        
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        #create frequency list ranging from 0 to len(nums) : len(nums) + 1
        l = [[] for x in range(len(nums) + 1)] #index = frequency [0, 1, 2, .... len(nums) +1]

        for num, freq in freq_map.items():
            l[freq].append(num)

        
        ans = []
        
        #start at end and collect the numbers

        for i in range(len(l) - 1, 0, -1):            
            for x in l[i]:
                ans.append(x)

            if len(ans) == k:
                return ans

        


    




        
        