https://leetcode.com/problems/merge-sorted-array/description/
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        left = n - 1
        right = m - 1

        while left >= 0 and right >= 0:
            if nums1[right] > nums2[left]:
                nums1[right + left + 1] = nums1[right]
                right -= 1
            else:
                nums1[right + left + 1] = nums2[left]
                left -= 1
                
        while left >= 0:
            nums1[left] = nums2[left]
            left -= 1
        
        
