class Solution(object):
    def kClosest(self, points, k):
        value = []
        for point in points:
            dist = (point[0] ** 2) + (point[1] ** 2)
            value.append([dist, point[0], point[1]])

        value.sort()
        value = value[:k]
        result = []
        for v in value:
            result.append([v[1], v[2]])
        return result

        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
