class Solution(object):
    def searchRange(self, nums, target):
        def search(x):
            l=0
            r=len(nums)
            while l<r:
                m=(l+r)//2
                if nums[m]<x:
                    l=m+1
                else:
                    r=m
            return l
        l=search(target)
        r=search(target+1)-1
        if l<=r:
            return [l,r]
        return [-1,-1]
