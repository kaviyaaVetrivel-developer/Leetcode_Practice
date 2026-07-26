class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            n = sum(map(lambda x: int(x) ** 2, str(n)))

        return True
          