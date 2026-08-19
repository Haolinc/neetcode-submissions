class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for row in range(n):
            dup = set()
            for col in range(n):
                val = board[row][col]
                if val != '.' and val in dup:
                    return False;
                dup.add(val)
        
        for row in range(n):
            dup = set()
            for col in range(n):
                val = board[col][row]
                if val != '.' and val in dup:
                    return False;
                dup.add(val)
        
        for sectionX in range(0, 7, 3):
            for sectionY in range(0, 7, 3):
                dup = set()
                for row in range(sectionX, sectionX + 3):
                    for col in range(sectionY, sectionY + 3):
                        val = board[row][col]
                        if val != '.' and val in dup:
                            return False;
                        dup.add(val)
                    
        return True

