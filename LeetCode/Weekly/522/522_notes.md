# 1. Minimum Rotations to Dial a Number

**Approach:** Greedy

**Problem:** Dial a string of digits using a circular dial (0–9), starting at 0. Minimize total rotations.

**Formula:**  
`d(a,b) = min(|a-b|, 10-|a-b|)`

**Logic:**
- Initialize `curr = 0`, `total = 0`.
- Iterate through each digit.
- Calculate minimum clockwise/anticlockwise distance.
- Add to `total` and update `curr`.

**Complexity:** O(n) time, O(1) space.

**Key takeaway:** On a circular structure, consider both directions and choose the shorter distance.

---

# 2. Minimum Rotations to Dial a Number II

**Approach:** Greedy + Incremental Computation

**Additional condition:** Reverse any suffix at most once.

**Brute force:** Try every suffix reversal and recalculate total → O(n²) → TLE.

**Key observations:**
- Reversing a suffix only changes the boundary transition.
- Internal transitions retain their costs because rotational distance is symmetric: `d(a,b) = d(b,a)`.
- Doing nothing is equivalent to `k = n-1`.

**Optimization:**

Let:
- `total` = original rotation cost.
- `prev` = digit before suffix (0 if k = 0).
- `first` = digit at index k.
- `last` = final digit of s.

`newCost = total - d(prev, first) + d(prev, last)`

**Logic:**
1. Calculate original cost.
2. Iterate through all possible k.
3. Subtract old boundary cost.
4. Add new boundary cost.
5. Maintain minimum answer.

**Complexity:** O(n) time, O(1) space.

**Key takeaway:** Calculate only the change caused by an operation instead of recomputing the entire result.