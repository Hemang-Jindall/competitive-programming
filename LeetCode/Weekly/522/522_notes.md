Minimum Rotations to Dial a Number

**1. Minimum Rotations to Dial a Number I**
- **Approach:** Greedy
- **Problem:** Dial a string of digits (0–9), starting at 0, using minimum rotations.
- **Formula:** `d(a,b) = min(abs(a-b), 10-abs(a-b))`
- **Logic:**
  1. Initialize `curr = 0`, `total = 0`.
  2. Iterate through each digit.
  3. Calculate minimum clockwise/anticlockwise distance.
  4. Add to `total` and update `curr`.
- **Complexity:** O(n) time, O(1) space.
- **Takeaway:** On a circular structure, choose the shorter direction.

---

**2. Minimum Rotations to Dial a Number II**
- **Approach:** Greedy + Incremental Computation
- **Additional Condition:** Reverse any suffix at most once.
- **Brute Force:** Try every suffix reversal and recalculate total → O(n²) → TLE.
- **Key Observations:**
  - Reversing a suffix only changes the boundary transition.
  - Internal costs remain unchanged due to symmetry: `d(a,b) = d(b,a)`.
  - Doing nothing is equivalent to `k = n-1`.
- **Optimization:** `newCost = total - d(prev, first) + d(prev, last)`
- **Variables:**
  - `total` = original rotation cost.
  - `prev` = digit before suffix (0 if k = 0).
  - `first` = digit at index k.
  - `last` = final digit of s.
- **Logic:**
  1. Calculate original rotation cost.
  2. Iterate through all possible k.
  3. Subtract old boundary cost.
  4. Add new boundary cost.
  5. Maintain minimum answer.
- **Complexity:** O(n) time, O(1) space.
- **Takeaway:** Calculate only what changes instead of recomputing everything.