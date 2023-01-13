class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
    
        def swap(n1, n2):
            matrix[n1[0]][n1[1]], matrix[n2[0]][n2[1]] = matrix[n2[0]][n2[1]], matrix[n1[0]][n1[1]]
    
        for i in range(len(matrix)//2):     
            for j in range(i, len(matrix)-i-1):
                swap([i, len(matrix)-j-1], [j, i])
                swap([j, i], [len(matrix)-i-1, j])
                swap([len(matrix)-i-1, j], [len(matrix)-j-1, len(matrix)-i-1])