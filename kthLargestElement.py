class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        nums.sort()
        nums[::-1]
        return nums[len(nums)-k]
