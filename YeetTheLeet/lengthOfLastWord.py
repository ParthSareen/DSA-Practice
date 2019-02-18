class Solution:
    def lengthOfLastWord(self, s: 'str') -> 'int':
        l = s.split()
        if len(l) == 0:
            return 0
        last = len(l) - 1
        return len(l[last])
