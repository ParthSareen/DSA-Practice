#if sorted
class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        n = len(nums)
        ans = []
        kill = True
        i = 0
        a = nums
        nums = sorted(nums)
        print(nums)
        while i < n-1 or kill:
            if i == n-1:
                print("no sol found")
                kill = False
#                return ans #empty string
            elif nums[i] + nums[n-1] == target:
                ans = [i, n-1]
                #print(ans)
                return ans

            elif nums[i] + nums[n-1] < target:
                i += 1

            elif nums[i] + nums[n-1] > target:
                n -= 1

            else:
                print("no sol found")
                kill = False
                return ans #empty string
            print(i,n-1)
        for counter, j in enumerate(nums)
object = Solution()
print(object.twoSum([3,2,4],6))
