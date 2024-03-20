# https://leetcode.com/problems/majority-element/description/
class Solution(object):
    def majorityElement(self, nums):
        mpp =defaultdict(int)
        for num in nums:
            mpp[num] += 1

        for num, count in mpp.items():
            if count > (len(nums) // 2):
                return num

        return -1
