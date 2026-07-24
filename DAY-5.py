class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0

        if x < 0:
            neg = x * -1
        else:
            neg = x

        while neg > 0:
            digit = neg % 10
            reverse = reverse * 10 + digit
            neg = neg // 10

        if x < 0:
            reverse = -reverse

        return reverse