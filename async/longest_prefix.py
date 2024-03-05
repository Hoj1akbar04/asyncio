from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum = min(strs)
        maximum = max(strs)
        i = 0
        while i < len(minimum) and minimum[i] == maximum[i]:
            i += 1
        return minimum[:i]


solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
