class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0
        s = ''
        while n // 2 != 0:
            s += str(n % 2)
            n = n // 2
        s += '1'
        f = 32 - len(s)
        s = str(0)*f + s[::-1]
        s = s[::-1]        
        for i in range(len(s)):
            if s[i] == '1':
                s = s[i:]
                break
        c = len(s) - 1
        number = 0
        for i in range(len(s)):
            if s[i] == '1':
                number += 2**c
            c -= 1
        return number
    