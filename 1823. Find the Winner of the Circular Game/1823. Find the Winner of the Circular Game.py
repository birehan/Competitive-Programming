class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        def helper(friends, pointer):
            while len(friends) != 1:
                pointer = (pointer + k - 1) % len(friends)
                friends.pop(pointer)
            return friends[0]

        friends = []
        for i in range(1, n + 1):
            friends.append(i)

        return helper(friends, 0)