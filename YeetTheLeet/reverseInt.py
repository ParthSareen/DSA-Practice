class Solution:
    def reverse(self, x: 'int') -> 'int':
        a = str(x)[::-1]
        if x < 0:
            res = int('-{0}'.format(a[:-1]))
        else:
            res = int(a)
        if res <= 2**31 -1 and res >= -2**31:
            return res
        return 0
