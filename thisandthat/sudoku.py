import random


class Sudoku:
    def __init__(self, _level = 5):
        self.board = [[0] * 9 for _ in range(9)]
        self._row = [[False] * 10 for _ in range(10)]
        self._col = [[False] * 10 for _ in range(10)]
        self._box = [[False] * 10 for _ in range(10)]
        self._pos = []
        # self._initBoard()
        self.level = min(_level, 10) / 20
        self._blankXY()
        self._blank = len(self._pos)


    #
    def _blankXY(self):
        count = 0
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if col == 0:
                    self._pos.append([i, j])
                    count += 1
        return count

    def _dfs(self, depth):
        if depth == self._blank:
            self.printBoard()
            self._makeBlank()
            count = self._blankXY()
            print(count)
            self.printBoard()
            exit(0)

        r, c = self._pos[depth]
        q = [i for i in range(1,10)]
        random.shuffle(q)
        for n in q:
            if self._condition(r, c, n):
                self._row[r][n] = self._col[c][n] = self._box[r // 3 * 3 + c // 3][n] = True
                self.board[r][c] = n
                self._dfs(depth + 1)
                self._row[r][n] = self._col[c][n] = self._box[r // 3 * 3 + c // 3][n] = False
                self.board[r][c] = 0


    def _condition(self, r, c, n):
        return not self._row[r][n] and not self._col[c][n] and not self._box[r // 3 * 3 + c // 3][n]

    def _prob(self):
        return random.random() < self.level + 0.3


    def _makeBlank(self):
        for r in range(9):
            for c in range(9):
                if self._prob():
                    self.board[r][c] = 0


    def setBoard(self):
        self.board = [list(map(int, input().split())) for _ in range(9)]
        self._dfs(0)

    def makeBoard(self):
        self._dfs(0)

    def printBoard(self):
        print("┏ " + "━"*17 + " ┓")
        for row in self.board:
            print("┃", end=" ")
            for col in row:
                print(col, end=" ")
            print("┃")
        print("┗ " + "━" * 17 + " ┛")
        print()

if __name__ == "__main__":
    s = Sudoku()
    s.makeBoard()

