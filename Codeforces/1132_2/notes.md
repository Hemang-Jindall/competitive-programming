CF 2284B - Introduction to the Niche Internet
Goal: reorder so exactly k donations are >= the average of those before them.

1. Every copy of the max is always pleasant. If it appears c times and c > k -> NO.
2. Going up, everything is pleasant. Going down, only copies of the max are.
3. So: the k largest ascending, then the rest descending.

Example: 1 2 3 4 5, k=3 -> 3 4 5 2 1
Status: needed a solution online. Redo cold.

WHERE I GOT STUCK

- Didn't see why "k largest ascending, rest descending" gives exactly k.
  Ascending: each >= everything before -> all pleasant.
  Descending: only copies of the max are pleasant, so leftovers fail (needs k >= c).
- arr[:k][::-1] + arr[k:] -> slice top k, reverse, glue leftovers on.
- print(\*list) unpacks the list, prints space-separated.
- Should have brute-forced small cases (permutations, n <= 8): min count = c, max = n.
