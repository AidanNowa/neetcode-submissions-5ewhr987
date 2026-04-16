class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        counts = [0] * len(temperatures)
        temp_index_pairs = []
        for i in range(len(temperatures)):
            while len(temp_index_pairs) != 0 and temperatures[i] > temp_index_pairs[-1][0]:
                top = temp_index_pairs.pop()
                counts[top[1]] = i - top[1]
            temp_index_pairs.append((temperatures[i], i))
        return counts

        