class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        n = len(nums)
        ans = []
        final = []
        kill = True
        i = 0
        a = nums
        nums = sorted(nums)
        print(nums)
        while i < n and kill:
            print(i,n-1)
            if i == n-1:
                print("no sol found")
                kill = False
                return  None#empty string
            elif nums[i] + nums[n-1] == target:
                ans = [nums[i], nums[n-1]]
                print(ans)
                #return ans
                kill = False

            elif nums[i] + nums[n-1] < target:
                i += 1

            elif nums[i] + nums[n-1] > target:
                n -= 1

            else:
                print("no sol found")
                kill = False
                return ans #empty string

        b = set(ans)
        return [j for j, item in enumerate(a) if item in b]

object = Solution()
print(object.twoSum([3,2,4],9))
