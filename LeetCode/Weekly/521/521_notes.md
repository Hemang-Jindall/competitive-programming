Minimum Rotations to Dial a Number

**1. Dial a Number I**
- Approach: Greedy
- Logic: Always choose the shorter direction on the circular dial.
- Formula: `min(abs(a-b), 10-abs(a-b))`
- Complexity: O(n) time, O(1) space.
- Takeaway: Choose the minimum cost at each step.

**2. Dial a Number II**
- Approach: Greedy + Incremental Computation
- Logic: Reversing a suffix only changes the boundary transition; internal costs remain unchanged due to symmetry.
- Formula: `newCost = total - d(prev, first) + d(prev, last)`
- Complexity: O(n) time, O(1) space.
- Takeaway: Recalculate only what changes instead of recomputing everything.