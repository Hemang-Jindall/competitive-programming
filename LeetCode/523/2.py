class Solution(object):
    def maxPrimes(self, n, s):
        def is_prime(x):
            if x < 2:
                return False

            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False

            return True

        total = 0
        i = 2
        primes = []

        while i <= s and len(primes) < n:
            if is_prime(i):
                if total + i > s:
                    break

                total += i
                primes.append(i)

            i += 1

        return primes

#what haved you learned from this problem?
#one thing is that I probably would have found the solution honestly, let's next time try to look for what all we know within the problem. We also found out the prime function as well.
#tomorrow, we're going to try to do this problem again all on our own. 