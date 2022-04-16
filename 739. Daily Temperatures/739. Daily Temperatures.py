class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        result = [0] * len(temperatures)

        for i in range(0, len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return result
