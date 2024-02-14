class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        rev = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x != 0:
            digit = x % 10
            new_rev = rev * 10 + digit

            if new_rev > INT_MAX or new_rev < INT_MIN:
                return 0
            rev = new_rev
            x = x // 10
        return sign * rev
