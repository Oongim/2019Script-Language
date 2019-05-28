# 11-20 과 12-13은 같이 구현한다.
from tkinter import *

GAME_ROW = 6
GAME_COL = 5

PLAYER_O = 0
PLAYER_X = 1
PLAYER_EMPTY = 2
PLAYER_CANT_PUSH = 3

END_WIN_O = PLAYER_O
END_WIN_X = PLAYER_X
END_DRAW = 4
NOT_END = 5

STANDARD_NUM_CONTINUOUS_TOKENS_FOR_END = 4

class Cell:
    manager = None
    imageList = []

    @staticmethod
    def initClassCell(manager):
        Cell.imageList = []
        Cell.imageList.append(PhotoImage(file="image/o.gif"))
        Cell.imageList.append(PhotoImage(file="image/x.gif"))
        Cell.imageList.append(PhotoImage(file="image/empty.gif"))
        Cell.manager = manager

    def __init__(self, frame, row, col):
        self.row = row
        self.col = col
        self.button = Button(frame, image=Cell.imageList[PLAYER_EMPTY], command=lambda cell=self: self.manager.pressed(cell))
        self.button.grid(row=col, column=row)
        self.token = PLAYER_EMPTY

    def canPush(self):
        if self.token == PLAYER_EMPTY:
            return True
        return False

    def push(self, player):
        self.token = player
        self.button.configure(image=self.imageList[player])

    def unable(self):
        self.token = PLAYER_CANT_PUSH


class Samoc:
    endCells = []
    def checkAllCellPushed(self):
        for cell in self.cellList:
            if cell.token == PLAYER_EMPTY:
                return False
        return True

    def checkGameEnd(self):

        # 각 열의 줄을 검사
        for r in range(GAME_ROW):
            Samoc.endCells.clear()
            numContinuousTokens = 0
            kindContinuousTokens = self.cellList[r].token
            for c in range(GAME_COL):     
                if kindContinuousTokens == self.cellList[c*GAME_ROW + r].token:
                    numContinuousTokens += 1
                    Samoc.endCells.append(self.cellList[c*GAME_ROW + r])
                else:
                    numContinuousTokens = 1
                    kindContinuousTokens = self.cellList[c*GAME_ROW + r].token
                    Samoc.endCells = [self.cellList[c * GAME_ROW + r]]

                if numContinuousTokens >= STANDARD_NUM_CONTINUOUS_TOKENS_FOR_END:
                    if kindContinuousTokens == PLAYER_O or kindContinuousTokens == PLAYER_X:
                        return kindContinuousTokens


        # 각 행의 줄을 검사
        for c in range(GAME_COL):
            Samoc.endCells.clear()
            numContinuousTokens = 0
            kindContinuousTokens =  self.cellList[c * GAME_ROW].token
            for r in range(GAME_ROW):               

                if kindContinuousTokens == self.cellList[c * GAME_ROW + r].token:
                    numContinuousTokens += 1
                    Samoc.endCells.append(self.cellList[c * GAME_ROW + r])
                else:
                    numContinuousTokens = 1
                    kindContinuousTokens = self.cellList[c * GAME_ROW + r].token
                    Samoc.endCells = [self.cellList[c * GAME_ROW + r]]

                if numContinuousTokens >= STANDARD_NUM_CONTINUOUS_TOKENS_FOR_END:
                    if kindContinuousTokens == PLAYER_O or kindContinuousTokens == PLAYER_X:
                        return kindContinuousTokens

        
        # 우하로 내려가는 대각선 - 열에서 시작
        for r in range(GAME_ROW):
            Samoc.endCells.clear()
            c = 0
            numContinuousTokens = 0
            kindContinuousTokens = self.cellList[c * GAME_ROW + r].token
            while True:
                if not (0 <= r < GAME_ROW and 0 <= c < GAME_COL):
                    break

                if kindContinuousTokens == self.cellList[c * GAME_ROW + r].token:
                    numContinuousTokens += 1
                    Samoc.endCells.append(self.cellList[c * GAME_ROW + r])
                else:
                    numContinuousTokens = 1
                    kindContinuousTokens = self.cellList[c * GAME_ROW + r].token
                    Samoc.endCells = [self.cellList[c * GAME_ROW + r]]

                if numContinuousTokens >= STANDARD_NUM_CONTINUOUS_TOKENS_FOR_END:
                    if kindContinuousTokens == PLAYER_O or kindContinuousTokens == PLAYER_X:
                        return kindContinuousTokens
                r += 1
                c += 1

        # 우하로 내려가는 대각선 - 행에서 시작
        for c in range(GAME_COL):
            Samoc.endCells.clear()
            r = 0
            numContinuousTokens = 0
            kindContinuousTokens = self.cellList[c * GAME_ROW + r].token
            while True:
                if not (0 <= r < GAME_ROW and 0 <= c < GAME_COL):
                    break

                if kindContinuousTokens == self.cellList[c * GAME_ROW + r].token:
                    numContinuousTokens += 1
                    Samoc.endCells.append(self.cellList[c * GAME_ROW + r])
                else:
                    numContinuousTokens = 1
                    kindContinuousTokens = self.cellList[c * GAME_ROW + r].token
                    Samoc.endCells = [self.cellList[c * GAME_ROW + r]]

                if numContinuousTokens >= STANDARD_NUM_CONTINUOUS_TOKENS_FOR_END:
                    if kindContinuousTokens == PLAYER_O or kindContinuousTokens == PLAYER_X:
                        return kindContinuousTokens
                r += 1
                c += 1

        # 좌하로 내려가는 대각선 - 열에서 시작
        for r in range(GAME_ROW):
            Samoc.endCells.clear()
            c = 0
            numContinuousTokens = 0
            kindContinuousTokens = self.cellList[c * GAME_ROW + r].token
            while True:
                if not (0 <= r < GAME_ROW and 0 <= c < GAME_COL):
                    break

                if kindContinuousTokens == self.cellList[c * GAME_ROW + r].token:
                    numContinuousTokens += 1
                    Samoc.endCells.append(self.cellList[c * GAME_ROW + r])
                else:
                    numContinuousTokens = 1
                    kindContinuousTokens = self.cellList[c * GAME_ROW + r].token
                    Samoc.endCells = [self.cellList[c * GAME_ROW + r]]

                if numContinuousTokens >= STANDARD_NUM_CONTINUOUS_TOKENS_FOR_END:
                    if kindContinuousTokens == PLAYER_O or kindContinuousTokens == PLAYER_X:
                        return kindContinuousTokens
                r -= 1
                c += 1

        # 좌하로 내려가는 대각선 - 행에서 시작
        for c in range(GAME_COL):
            Samoc.endCells.clear()
            r = GAME_ROW-1
            numContinuousTokens = 0
            kindContinuousTokens = self.cellList[c * GAME_ROW + r].token
            while True:
                if not (0 <= r < GAME_ROW and 0 <= c < GAME_COL):
                    break

                if kindContinuousTokens == self.cellList[c * GAME_ROW + r].token:
                    numContinuousTokens += 1
                    Samoc.endCells.append(self.cellList[c * GAME_ROW + r])
                else:
                    numContinuousTokens = 1
                    kindContinuousTokens = self.cellList[c * GAME_ROW + r].token
                    Samoc.endCells = [self.cellList[c * GAME_ROW + r]]

                if numContinuousTokens >= STANDARD_NUM_CONTINUOUS_TOKENS_FOR_END:
                    if kindContinuousTokens == PLAYER_O or kindContinuousTokens == PLAYER_X:
                        return kindContinuousTokens
                r -= 1
                c += 1


        if self.checkAllCellPushed():
            return END_DRAW

        return NOT_END




    def endGame(self, winner):
        self.gameEnd = True
        for cell in self.cellList:
            cell.unable()

        if winner == END_WIN_O or winner == END_WIN_X:
            self.turnLabel.update()
            try:                # 종료시 에러를 방지하는 코드
                while True:
                    for cell in Samoc.endCells:
                        if cell.token == PLAYER_CANT_PUSH:
                            flickeringImage = winner
                            cell.token = winner
                        else:
                            flickeringImage = PLAYER_EMPTY
                            cell.token = PLAYER_CANT_PUSH
                        cell.button.configure(image=Cell.imageList[flickeringImage])
                        cell.button.image = Cell.imageList[flickeringImage]
                        cell.button.update()
                    Samoc.endCells[0].button.after(250)
            except:
                pass


    def pressed(self, cell):
        if not self.gameEnd:
            dstCell = self.getPushableCellAtRow(cell.row)
            if not dstCell == None:
                if self.turn == PLAYER_O:  # 0 차례
                    dstCell.push(PLAYER_O)
                    self.turnLabel.configure(text="o 차례")

                elif self.turn == PLAYER_X:
                    dstCell.push(PLAYER_X)
                    self.turnLabel.configure(text="x 차례")

                self.turn = not self.turn



            isGameEnd = self.checkGameEnd()
            if isGameEnd == END_WIN_O:
                self.turnLabel.configure(text="o 의 승리입니다.")
                self.endGame(isGameEnd)

            elif isGameEnd == END_WIN_X:
                self.turnLabel.configure(text="x 의 승리입니다.")
                self.endGame(isGameEnd)

            elif isGameEnd == END_DRAW:
                self.turnLabel.configure(text="비겼습니다.")
                self.endGame(isGameEnd)



    def getPushableCellAtRow(self, row):
        for c in range(GAME_COL-1, 0-1, -1):
            if self.cellList[c * GAME_ROW + row].canPush():
                return self.cellList[c * GAME_ROW + row]
        return None




    def __init__(self):
        window = Tk()
        Cell.initClassCell(self)
        frame1 = Frame(window)
        frame1.pack()
        self.turn = PLAYER_O
        self.cellList = []
        for c in range(GAME_COL):
            for r in range(GAME_ROW):
                self.cellList.append(Cell(frame1, r, c))

        frame2 = Frame(window)
        frame2.pack()

        self.turnLabel = Label(frame2, text="o 차례")
        self.turnLabel.pack()

        self.gameEnd = False
        window.mainloop()

Samoc()