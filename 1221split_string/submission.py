class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num_r = 0
        num_l = 0
        count = 0
        for c in s:
            if c == 'R': num_r += 1
            else: num_l += 1
            if num_r == num_l:
                num_r = 0
                num_l = 0
                count += 1
        return count
