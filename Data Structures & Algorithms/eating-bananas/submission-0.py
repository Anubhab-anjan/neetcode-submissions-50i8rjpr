class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for p in piles:
                hours += -(-p // mid)  # same as math.ceil(p/mid)

            if hours <= h:
                res = mid
                right = mid - 1  # try smaller speed
            else:
                left = mid + 1   # need larger speed

        return res
