class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            new_full = empty // numExchange
            total += new_full
            empty = empty % numExchange + new_full

        return total
        