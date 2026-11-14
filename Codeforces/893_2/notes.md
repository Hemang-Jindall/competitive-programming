# CF 1858B - The Walkway

**Goal:** Minimize the total number of cookies Petya eats after removing exactly one seller, and find the number of removals that achieve this minimum.

## Initial Idea

1. Calculate the number of additional cookies Petya needs between every pair of consecutive sellers using the distance between their positions and `d`.
2. Calculate the initial and final contributions separately, since the beginning and end of the walkway behave differently from internal gaps.
3. For each seller, consider removing it. This merges its two neighbouring gaps into one larger gap (or changes a boundary contribution if it's the first or last seller).
4. Instead of recalculating the entire walkway for every removal, precompute gap contributions and update only the affected gaps.
5. Track the minimum number of cookies eaten and the number of removals that achieve it.