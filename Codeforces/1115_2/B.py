# Category: Greedy
# Constraints: t large, values big -> need O(n) per test case.
# First instinct: Sort the array and compare the two middle elements.
# Other approach: Separate elements by parity of their positions and compare the ranges.
# Gotcha: Sorting destroys positional information. The condition depends on which elements are at odd/even positions, not just on their values.

    