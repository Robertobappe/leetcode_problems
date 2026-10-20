class Solution:
    def hammingWeight(self, n: int) -> int:
        t = {'1':0}

        while n//2 != 0:
            if n % 2 == 1:
                t['1'] += 1
            n = n//2
        t['1'] += 1
        return t['1']