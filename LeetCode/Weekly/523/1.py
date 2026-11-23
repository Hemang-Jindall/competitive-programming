class Solution(object):
    def threeFibonacciSum(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 2 != 0:
            return False

        a = 0
        b = 1

        n = n//2

        while (a<n):
            a, b = b, a+b

        return n == a