## 초기상태 랜덤하게 설정
## 1부터9 까지의 리스트를 셔플한 후에, 초기 board 의 row, col, box 에 랜덤하게 배치
## fin
## 사용 안하게 된 Sudoku 의 메소드
import random

def _initBoard(self):
    randNums = [i for i in range(1, 10)]
    random.shuffle(randNums)
    seed = random.randrange(3)
    index = random.randrange(9)
    if seed == 0:  # col
        print("col!")
        for i in range(9):
            self.board[i][index] = randNums[i]
    elif seed == 1:  # row
        print("row!")
        self.board[index] = randNums
    else:  # box
        print("box!")
        r = index // 3 * 3
        c = index % 3 * 3
        k = 0
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                self.board[i][j] = randNums[k]
                k += 1