class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()

        coords = sorted(set(end for start, end in intervals))

        bit = [0] * (len(coords) + 1)

        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & -i
            return total

        def lower_bound(arr, target):
            left, right = 0, len(arr)

            while left < right:
                mid = (left + right) // 2

                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left

        ans = 0
        processed = 0

        for start, end in intervals:
            idx = lower_bound(coords, start)

            # Number of previous endpoints < start
            non_overlapping = query(idx)

            ans += processed - non_overlapping

            rank = lower_bound(coords, end) + 1
            update(rank)

            processed += 1

        return ans

#have to understand this question better