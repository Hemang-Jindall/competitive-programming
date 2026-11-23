class Solution(object):
    def calculateScore(self, a, b):
        a_n = 0
        b_n = 0

        while a > 0:
            a_n += a % 2
            a //= 2

        while b > 0:
            b_n += b % 2
            b //= 2

        if b_n > a_n:
            return b_n // a_n
        else:
            return b_n * a_n