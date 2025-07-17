class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_possible = max(candies)
        res = []

        for candy in candies:
            res.append(candy + extraCandies >= max_possible)

        return (res)