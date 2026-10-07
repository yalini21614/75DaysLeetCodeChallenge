class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        total=0
        answer=len(nums)+1
        for right in range(len(nums)):
            total+= nums[right]
            while total>=target:
                answer=min(answer,right-left+1)
                total-=nums[left]
                left+=1
        if answer==len(nums)+1:
            return 0
        return answer                   