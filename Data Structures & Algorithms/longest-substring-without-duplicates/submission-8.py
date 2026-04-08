class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = []
        curr_substring = []
        i = 0
        while i < len(s):
            # print(f"starting loop with: {i}, {s[i]}")
            if s[i] in curr_substring:
                if len(curr_substring) > len(max_substring):
                    max_substring = curr_substring
                # print(f"Curr i: {i}, sub_len: {len(curr_substring)}, curr_substring: {curr_substring}")
                i -= len(curr_substring) - 1
                # print(f"starting window again at i:{i}, letter:{s[i]}")
                curr_substring = [s[i]]
            else:
                curr_substring.append(s[i])
            i += 1
        # print(f"final string: {curr_substring}")
        if len(curr_substring) > len(max_substring):
            max_substring = curr_substring
        return len(max_substring)

        