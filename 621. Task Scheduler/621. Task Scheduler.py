from collections import Counter


class Solution(object):
    def leastInterval(self, tasks, n):
        counter = Counter(tasks)
        sorted_counter = sorted(counter.values())

        most_occur = sorted_counter[-1]
        freq = Counter(sorted_counter)

        count = freq[most_occur]
        result = max(((most_occur - 1) * (n + 1) + count), len(tasks))

        return result