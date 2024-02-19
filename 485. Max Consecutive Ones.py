
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c=0
        maximum=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
            else:
                
                c=0
            maximum=max(maximum,c)
        return maximum
