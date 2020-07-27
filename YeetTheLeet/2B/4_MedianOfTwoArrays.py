class Solution:
    def endSol(self, q):
        if len(q) % 2 == 0:
            return (q[(len(q)-1)//2] + q[(len(q))//2])/2
        else:
            return q[(len(q)-1)//2]
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        q = []
        i, j = 0, 0
        no_break = True
        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        elif len(nums1) == 0:
            return self.endSol(nums2)
        elif len(nums2) == 0:
            return self.endSol(nums1)
            
        while no_break:
            if nums1[i] < nums2[j]:
                q.append(nums1[i])
                if i+1 > len(nums1) - 1:
                    q = q + nums2[j:len(nums2)]
                    # print("i added break, q:", q)
                    no_break = False
                else:
                    i += 1
            else:
                q.append(nums2[j])
                if j + 1 > len(nums2) - 1:
                    q = q + nums1[i:len(nums1)]
                    # print("j added break, q:", q)
                    no_break = False
                else:
                    j += 1
        # print(q)
        return self.endSol(q)
        
        
