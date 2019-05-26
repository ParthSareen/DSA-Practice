class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        ans = nums1 + nums2
        ans.sort()
        print(ans)

        if len(ans)%2 == 1:
            index = int((len(ans) -0.5)//2)
            median = ans[index]
            return median
        elif len(ans)%2 == 0:
            index = int((len(ans)-0.5)//2)
            l_to_med = index
            r_to_med = index + 1
            median = (ans[l_to_med] + ans[r_to_med])/2
            return median
