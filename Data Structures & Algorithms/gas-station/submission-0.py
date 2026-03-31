class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        res=0
        srt=0
        for i in range(n):
            res += gas[i] - cost[i]
            if res<0:
                srt = i+1
                res=0
        return srt