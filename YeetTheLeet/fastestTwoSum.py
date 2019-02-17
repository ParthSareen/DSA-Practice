class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if dict.get(complement) is not None:
                return [i, dict[complement]]

            dict[nums[i]] = i

        raise ValueError("No solution")
obj = Solution()
print(obj.twoSum([2,3,5,6,7,8],11))
