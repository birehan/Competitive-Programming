class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        moves = [0] * len(boxes)
        forward_boxes = backward_boxes = 0
        forward_move = backward_move = 0
        
        for i in range(len(boxes)):
            moves[i] += forward_move
            moves[-i-1] += backward_move
            
            forward_boxes += int(boxes[i])
            backward_boxes += int(boxes[-i-1])
            
            forward_move += forward_boxes
            backward_move += backward_boxes
        
        return moves
            
        