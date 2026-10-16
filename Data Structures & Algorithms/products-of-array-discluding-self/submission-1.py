class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [1] * n

        #prefix product
        pre = n * [1]

        running = 1
        
        for i in range(n):
            pre[i] = running
            running *= nums[i]


        #post fix
        post = n * [1]

        running2 = 1
        for i in range(n-1, -1, -1):
            post[i] = running2
            running2 *= nums[i]


        for i in range(n):
            ans[i] = pre[i] * post[i]

        return ans