class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            s = set()
            for j in range(9):
                number = board[i][j]
                if number in s:
                    return False
                elif number != ".":
                    s.add(number)

        for i in range(9):
            s = set()
            for j in range(9):
                number = board[j][i]
                if number in s:
                    return False
                elif number != ".":
                    s.add(number)
        
        sub_box_coordinates = [
            (0,0),(0,3),(0,6),
            (3,0),(3,3),(3,6),
            (6,0),(6,3),(6,6)
        ]

        for i,j in sub_box_coordinates:
            s = set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    number = board[row][col]
                    if number in s:
                        return False
                    elif number != ".":
                        s.add(number)
        return True









