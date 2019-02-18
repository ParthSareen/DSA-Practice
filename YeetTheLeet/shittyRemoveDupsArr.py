class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        print(len(nums))
        i = 0
        if len(nums) == 2:
            if nums[i] == nums[i+1]:
                nums.pop(i)
        else:
            while i < len(nums):
                #print([i, i+1])
                if (i + 1) > len(nums)-1:
                    return len(nums)
                while nums[i] == nums[i+1]:
                    print([i,i+1])
                    nums.pop(i)
                    if i+1 > len(nums)-1:
                        break
                i += 1
        return len(nums)
