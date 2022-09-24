#--- MODULES ---#
from typing import Tuple, Union, List
from rich.console import Console
import pyfiglet



#--- STATEMENTS ---#
class Player: ...
class Seeker: ...
class Matrix: ...
class Game: ...



class Player:
    def __init__(self, identifier: str, console: Console, matrix: Matrix) -> None: ...
    def inputCoordinate(self) -> Tuple[int]: ...
    def getScore(self) -> int: ...
    def calcScore(self) -> None: ...
    def runTurn(self, round:int) -> bool: ...


class Seeker:
    def __init__(self, identifier: str, matrix: Matrix) -> None: ...
    def calcScore(self) -> int: ...
    def checkRows(self) -> int: ...
    def checkRow(self, index: int) -> int: ...
    def checkColumns(self) -> int: ...
    def checkColumn(self, index: int) -> int: ...
    def checkDiagonals(self) -> int: ...


class Matrix:
    COLOR_PLAYER_X = 'green'
    COLOR_PLAYER_O = 'yellow'
    def __init__(self, game: Game, dimension: int, console: Console) -> None: ...
    def createMatrix(self) -> None: ...
    def printHeader(self, round:int) -> None: ...
    def printMatrix(self, rowSelected: int = None) -> None: ...
    def setBox(self, row: int, col: int, player: str) -> bool: ...
    def getBox(self, row: int, col: int) -> Union[str, None]: ...
    def matrixIsFull(self) -> bool: ...
    def rowIsFull(self, index: int) -> bool: ...
    def boxIsFull(self, row: int, column: int) -> bool: ...
    def getDimension(self) -> int: ...


class Game:
    PLAYER_X = 'X'
    PLAYER_O = 'O'
    KILO_POINTS = 2
    MEGA_POINTS = 5
    GIGA_POINTS = 10
    TERA_POINTS = 25
    PETA_POINTS = 50
    MAX_ROUND = 20
    MAX_SCORE = 100
    def __init__(self) -> None: ...
    def printTitle(self) -> None: ...
    def printTheEnd(self, message:str='Game Over') -> None: ...
    def inputBoardDimension(self) -> None: ...
    def addRount(self) -> bool: ...
    def getScore(self) -> Tuple[int]: ...
    def run(self) -> None: ...



#--- DEFINITIONS ---#
class Player:
    def __init__(self, identifier: str, console: Console, matrix: Matrix) -> None:
        self.identifier = identifier
        self.console = console
        self.matrix = matrix
        self.seeker = Seeker(self.identifier, self.matrix)
        self.score = 0
        self.round:int = None

    def inputCoordinate(self) -> Tuple[int]:
        """Return (row, col)"""
        ok = False
        row, col = 0, 0

        self.console.clear()
        self.matrix.printHeader(self.round)
        self.matrix.printMatrix()
        while not ok:
            try:
                row = int(self.console.input('Seleziona riga> '))-1
                if not 0 <= row < self.matrix.getDimension():
                    raise Exception()
            except:
                self.console.print('[*] Riga non valida\n', style='red')
                continue
            if self.matrix.rowIsFull(row):
                self.console.print('[*] Riga non valida\n', style='red')
            else:
                ok = True

        self.console.clear()
        self.matrix.printHeader(self.round)
        self.matrix.printMatrix(row)
        ok = False
        while not ok:
            try:
                col = int(self.console.input('Seleziona colonna> '))-1
                if not 0 <= col < self.matrix.getDimension():
                    raise Exception()
            except:
                self.console.print('[*] Colonna non valida\n', style='red')
                continue
            if self.matrix.boxIsFull(row, col):
                self.console.print('[*] Cella non valida\n', style='red')
            else:
                ok = True

        return row, col

    def getScore(self) -> int:
        return self.score

    def calcScore(self) -> None:
        self.score = self.seeker.calcScore()

    def runTurn(self, round:int) -> bool:
        """Return True if game is end"""
        if self.matrix.matrixIsFull():
            return True
        
        self.round = round
        row, col = self.inputCoordinate()
        self.matrix.setBox(row, col, self.identifier)
        self.calcScore()
        return (False if self.score < Game.MAX_SCORE else True)


class Seeker:
    def __init__(self, identifier: str, matrix: Matrix) -> None:
        self.identifier = identifier
        self.matrix = matrix

    def calcScore(self) -> int:
        tot = 0
        tot += self.checkRows()
        tot += self.checkColumns()
        tot += self.checkDiagonals()
        return tot

    def checkRows(self) -> int:
        tot = 0
        for i in range(self.matrix.getDimension()):
            tot += self.checkRow(i)
        return tot

    def checkRow(self, index: int) -> int:
        tot = 0
        count = 0
        for i in range(self.matrix.getDimension()):
            if self.matrix.getBox(index, i) == self.identifier:
                count += 1
            else:
                if count == self.matrix.getDimension():
                    tot += Game.PETA_POINTS
                elif count==5:
                    tot += Game.TERA_POINTS
                elif count==4:
                    tot += Game.GIGA_POINTS
                elif count==3:
                    tot += Game.MEGA_POINTS
                elif count==2:
                    tot += Game.KILO_POINTS
                count = 0
        else:
            if count == self.matrix.getDimension():
                tot += Game.PETA_POINTS
            elif count==5:
                tot += Game.TERA_POINTS
            elif count==4:
                tot += Game.GIGA_POINTS
            elif count==3:
                tot += Game.MEGA_POINTS
            elif count==2:
                tot += Game.KILO_POINTS
        return tot

    def checkColumns(self) -> int:
        tot = 0
        for i in range(self.matrix.getDimension()):
            tot += self.checkColumn(i)
        return tot

    def checkColumn(self, index:int) -> int:
        tot = 0
        count = 0
        for i in range(self.matrix.getDimension()):
            if self.matrix.getBox(i, index)==self.identifier:
                count += 1
            else:
                if count == self.matrix.getDimension():
                    tot += Game.PETA_POINTS
                elif count==5:
                    tot += Game.TERA_POINTS
                elif count==4:
                    tot += Game.GIGA_POINTS
                elif count==3:
                    tot += Game.MEGA_POINTS
                elif count==2:
                    tot += Game.KILO_POINTS
                count = 0
        else:
            if count == self.matrix.getDimension():
                tot += Game.PETA_POINTS
            elif count==5:
                tot += Game.TERA_POINTS
            elif count==4:
                tot += Game.GIGA_POINTS
            elif count==3:
                tot += Game.MEGA_POINTS
            elif count==2:
                tot += Game.KILO_POINTS
        return tot

    def checkDiagonals(self) -> int:
        dim = self.matrix.getDimension()
        tot = 0
        for i in range(1-dim, dim):
            temp = list()
            for j in range(0, dim):
                if 0<=j<dim and 0<=i+j<dim:
                    temp.append((j, (i+j)))
                else:
                    continue
            tot += self.checkDiagonal(temp)
        
        for i in range(0, (dim*2)-1):
            temp = list()
            for j in range(0, dim):
                if 0<=j<dim and 0<=i-j<dim:
                    temp.append((j, (i-j)))
                else:
                    continue
            tot += self.checkDiagonal(temp)
        return tot
    
    def checkDiagonal(self, elements:List[Tuple[int, int]]) -> int:
        tot = 0
        count = 0
        for row, col in elements:
            if self.matrix.getBox(row, col)==self.identifier:
                count += 1
            else:
                if count == self.matrix.getDimension():
                    tot += Game.PETA_POINTS
                elif count==5:
                    tot += Game.TERA_POINTS
                elif count==4:
                    tot += Game.GIGA_POINTS
                elif count==3:
                    tot += Game.MEGA_POINTS
                elif count==2:
                    tot += Game.KILO_POINTS
                count = 0
        else:
            if count == self.matrix.getDimension():
                tot += Game.PETA_POINTS
            elif count==5:
                tot += Game.TERA_POINTS
            elif count==4:
                tot += Game.GIGA_POINTS
            elif count==3:
                tot += Game.MEGA_POINTS
            elif count==2:
                tot += Game.KILO_POINTS
        return tot


class Matrix:
    COLOR_PLAYER_X = 'green'
    COLOR_PLAYER_O = 'yellow'

    def __init__(self, game:Game, dimension:int, console:Console) -> None:
        self.game = game
        self.dimension = dimension
        self.console = console
        self.board:List[List[str]] = list()

    def createMatrix(self) -> None:
        self.board = list()
        for _ in range(self.dimension):
            self.board.append([' ' for _ in range(self.dimension)])
    
    def printHeader(self, round:int) -> None:
        scoreX, scoreO = self.game.getScore()
        self.console.print(f'\n\tRound: {round}', end='')
        self.console.print(f'\tScores: [{Matrix.COLOR_PLAYER_X}]X[/{Matrix.COLOR_PLAYER_X}]: [purple]{scoreX}[/purple]', end='')
        self.console.print(f'\t[{Matrix.COLOR_PLAYER_O}]O[/{Matrix.COLOR_PLAYER_O}]: [purple]{scoreO}[/purple]\n')

    def printMatrix(self, rowSelected:int=None) -> None:
        self.console.print(' '*5, end='')
        [self.console.print(num+1, ' '*3, sep='', end='') for num in range(self.dimension)]
        self.console.print('\n', ' '*2, end='')
        self.console.print(bytes([201]).decode('cp437'), *[bytes([205, 205, 205, 203]).decode('cp437') for _ in range(self.dimension-1)], bytes([205, 205, 205, 187]).decode('cp437'), sep='')
        for row, index in zip(self.board, range(self.dimension)):
            self.console.print(f' {("[red]" if rowSelected==index else "")}{index+1} ', end='')
            for element in row:
                self.console.print(bytes([186]).decode('cp437'), end='')
                self.console.print(f' {element} ', end='', style=(Matrix.COLOR_PLAYER_X if element==Game.PLAYER_X else Matrix.COLOR_PLAYER_O))
            self.console.print(bytes([186]).decode('cp437'))
            if index<self.dimension-1:
                self.console.print(' '*3, bytes([204]).decode('cp437'), *[bytes([205, 205, 205, 206]).decode('cp437') for _ in range(self.dimension-1)], bytes([205, 205, 205, 185]).decode('cp437'), sep='')
        self.console.print(' '*3, bytes([200]).decode('cp437'), *[bytes([205, 205, 205, 202]).decode('cp437') for _ in range(self.dimension-1)], bytes([205, 205, 205, 188]).decode('cp437'), sep='')
    
    def setBox(self, row:int, col:int, player:str) -> bool:
        """Return False if that box is busy"""
        try:
            if self.board[row][col]==' ':
                self.board[row][col] = player
                return True
            else:
                return False
        except:
            return False
    
    def getBox(self, row:int, col:int) -> Union[str, None]:
        value = None
        try:
            value = self.board[row][col]
        except:
            value = None
        finally:
            return value

    def matrixIsFull(self) -> bool:
        for row in self.board:
            for element in row:
                if element==' ':
                    return False
        return True

    def rowIsFull(self, index:int) -> bool:
        """Return False only if num of row is valid and that row has at least one free element"""
        if not (0<=index<self.dimension):
            return True
        for element in self.board[index]:
            if element==' ':
                return False
        return True

    def boxIsFull(self, row:int, col:int) -> bool:
        """Return False only if coordinate is valid and that box is not busy"""
        if not (0<=row<self.dimension) and not (0<=col<self.dimension):
            return True
        if self.board[row][col]==' ':
            return False
        return True
    
    def getDimension(self) -> int:
        return self.dimension


class Game:
    PLAYER_X = 'X'
    PLAYER_O = 'O'
    KILO_POINTS = 2
    MEGA_POINTS = 5
    GIGA_POINTS = 10
    TERA_POINTS = 25
    PETA_POINTS = 50
    MAX_ROUND = 20
    MAX_SCORE = 100

    def __init__(self) -> None:
        self.dimension:int = None
        self.roundCounter:int = None

        self.console = Console()
        self.console.clear()
        self.printTitle('Setup Iniziale')
        self.inputBoardDimension()

        self.console.clear()
        self.matrix = Matrix(self, self.dimension, self.console)
        self.matrix.createMatrix()

        self.playerX = Player(Game.PLAYER_X, self.console, self.matrix)
        self.playerO = Player(Game.PLAYER_O, self.console, self.matrix)
    
    def printTitle(self, message:str='Benvenuto') -> None:
        result = pyfiglet.figlet_format('TicTacToe', font='slant') 
        self.console.print(f'[bold green]{result}[/bold green]')
        self.console.print('#'*49, style='bold green')
        self.console.print(' '*5, '#'*8, ' '*2, message, ' '*2, '#'*8, style='bold green')
        self.console.print('#'*49, style='bold green')
    
    def printTheEnd(self, message:str='Game Over') -> None:
        self.console.clear()
        result = pyfiglet.figlet_format("Game Over", font='slant')
        self.console.print(f'[purple3]{result}[/purple3]')
        self.console.print('#'*49, style='purple3')
        self.console.print(' '*5, '#'*8, ' '*2, message, ' '*2, '#'*8, style='purple3')
        self.console.print('#'*49, style='purple3')
        self.matrix.printHeader(self.roundCounter)
        self.matrix.printMatrix()
    
    def inputBoardDimension(self) -> None:
        ok = False
        while not ok:
            try:
                self.dimension = int(self.console.input('Dimensione matrice di gioco> '))
            except:
                self.console.print('[*] Dimensione non valida\n', style='red')
                continue
            if self.dimension>=3 and self.dimension<=9:
                ok = True
            else:
                self.console.print('[*] Dimensione non valida (> di 3 e < di 9)\n', style='red')
    
    def addRount(self) -> bool:
        """Return False if the round limit has been reached"""
        if self.roundCounter==Game.MAX_ROUND:
            return False
        else:
            self.roundCounter += 1
            return True
    
    def getScore(self) -> Tuple[int]:
        return self.playerX.getScore(), self.playerO.getScore()
    
    def run(self) -> None:
        """Game cycle"""
        self.roundCounter = 0
        while True:
            if not self.addRount():
                self.printTheEnd('Rounds Are Over')
                break
            elif self.playerX.runTurn(self.roundCounter):
                self.printTheEnd(f'Player {self.playerX.identifier} Won')
                break

            if not self.addRount():
                self.printTheEnd('Rounds Are Over')
                break
            elif self.playerO.runTurn(self.roundCounter):
                self.printTheEnd(f'Player {self.playerO.identifier} Won')
                break


#--- EXECUTION ---#
if __name__=='__main__':
    Game().run()
    input()
