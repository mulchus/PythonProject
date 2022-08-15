import tkinter
import random
¹
coord = [50, 150, 250]

class TicTacToe(tkinter.Canvas):
    def __init__(self, window):
        self.state = []
        self.NoneState = []
        self.gameover = False
        for i in range (0, 9):
            self.state.append(None)
        self.window = window
        self.canvas = super().__init__(window, width=300, height=300)
        self.bind('<Button-1>', self.click)
        self.pack()

    def draw_lines(self):
         self.create_line(100, 0, 100, 300, fill='grey')
         self.create_line(200, 0, 200, 300, fill='grey')
         self.create_line(0, 100, 300, 100, fill='grey')
         self.create_line(0, 200, 300, 200, fill='grey')
         
    def add_o(self, column, row):
        r = 30
        column = coord[column]
        row = coord[row]
        self.create_oval(column-r, row-r, column+r, row+r, width=5, outline='red')

    def add_x(self, column, row):
        l = 30
        column = coord[column]
        row = coord[row]
        self.create_line(column-l, row-l, column+l, row+l, width=5, fill='blue')
        self.create_line(column-l, row+l, column+l, row-l, width=5, fill='blue')
    
    def bot_move(self):
        self.NoneState = []
        for i in range (0, 9):
            if self.state[i] == None:
                self.NoneState.append(i)
        if len(self.NoneState) > 0:
            i = self.NoneState[random.randint(0, len(self.NoneState)-1)]
            y = i//3
            x = i - y*3
            self.add_o(x, y)
            self.state[i] = 'o'

    def click(self, event):
        while not self.gameover:
            x = event.x
            y = event.y
            if x in range (0, 101): x = 0
            elif x in range (101, 201): x = 1
            elif x in range (201, 301): x = 2
            if y in range (0, 101): y = 0
            elif y in range (101, 201): y = 1
            elif y in range (201, 301): y = 2
            if self.state[(x+3*y)] == None: 
                self.state[(x+3*y)] = 'x'
                self.add_x(x, y)
                
                if self.get_winner():
                    print('x_win')
                    self.gameover = True
                    
                elif None in self.state:
                    self.bot_move()
                    if self.get_winner():
                        print('o_win')
                        self.gameover = True
                else:
                    print('draw')
                    self.gameover = True
        
    def get_winner(self):
        def winer(winsimvol):
            if (str(self.state[0])+str(self.state[1])+str(self.state[2]) == winsimvol 
            or str(self.state[3])+str(self.state[4])+str(self.state[5]) == winsimvol 
            or str(self.state[6])+str(self.state[7])+str(self.state[8]) == winsimvol
            or str(self.state[6])+str(self.state[7])+str(self.state[8]) == winsimvol
            or str(self.state[0])+str(self.state[3])+str(self.state[6]) == winsimvol
            or str(self.state[1])+str(self.state[4])+str(self.state[7]) == winsimvol
            or str(self.state[2])+str(self.state[5])+str(self.state[8]) == winsimvol
            or str(self.state[0])+str(self.state[4])+str(self.state[8]) == winsimvol
            or str(self.state[6])+str(self.state[4])+str(self.state[2]) == winsimvol):
                if winsimvol == ('xxx'):
                    return 'x_win'
                elif winsimvol == ('ooo'):
                    return 'o_win'
                    
        print(len(self.NoneState), self.NoneState)
        
        if len(self.NoneState) > 1:
            if winer('xxx'): return 'x_win'
            elif winer('ooo'): return 'o_win'
        elif len(self.NoneState) == 1:
            return 'NoneNone'


                    

  
        #if len(self.NoneState) > 1:
        #    return(winer('ooo'))
        #elif len(self.NoneState) == 0:
        #    return
        #else: 
        #    poz = self.state.NoneState[0]
        #    self.state[poz] = 'o'
        #    if winer('ooo') != 'o_win':
        #        self.state[poz] = None
         #       return None
      
        #print(str(self.state[0:3]))
        
        
        
#print(TicTacToe)

window = tkinter.Tk()
game = TicTacToe(window)
#game.state = ['x', 'x', 'o', 'o', 'o', 'x', 'x', 'o', 'x']
#game.get_winner()
game.draw_lines()
#self.bind('<Button-1>', self.click)
#game.add_o(0, 2)
#game.add_x(2, 0)
window.mainloop()