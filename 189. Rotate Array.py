# https://leetcode.com/problems/rotate-array/
class Solution(object):
    def rotate(self, nums, k):

        temp = []
        k=k%len(nums)
        for i in range(len(nums)-k, len(nums)):
            temp.append(nums[i])

        i = len(nums) - 1
        while i > k - 1:
            nums[i] = nums[i - k]
            i -= 1

        for j in range(len(temp)):
            nums[j] = temp[j]

        return nums
