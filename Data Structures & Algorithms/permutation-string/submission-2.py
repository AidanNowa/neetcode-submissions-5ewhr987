class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = "".join(sorted(s1))
        left = 0
        right = len(s1)
        if len(s2) < len(s1):
            return False
        while right < len(s2) + 1:
            window = s2[left:right]
            sorted_window = "".join(sorted(window))
            # print(f"sorted s1: {sorted_s1}, sorted window: {sorted_window}")
            if sorted_window == sorted_s1:
                return True
            left += 1
            right += 1
        return False
        