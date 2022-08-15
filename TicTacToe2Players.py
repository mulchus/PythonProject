import tkinter
import time

coord = [50, 150, 250]

class TicTacToe(tkinter.Canvas):
    def __init__(self, window):
        self.reinit()
        self.window = window
        self.canvas = super().__init__(window, width=300, height=300)
        self.bind('<Button-1>', self.click)
        self.pack()

    #тут какой то комментарий
    def reinit(self):
        self.player = 'x'
        self.state = list([None]*9)
        self.NoneState = []
        self.gameover = False
        
    def draw_lines(self):
         self.create_line(100, 0, 100, 300, fill = 'grey')
         self.create_line(200, 0, 200, 300, fill = 'grey')
         self.create_line(0, 100, 300, 100, fill = 'grey')
         self.create_line(0, 200, 300, 200, fill = 'grey')
         
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
    
    #def bot_move(self):
    #    self.NoneState = []
    #    for i in range (0, 9):
    #        if self.state[i] == None:
    #           self.NoneState.append(i)
    #    if len(self.NoneState) > 0:
    #        i = self.NoneState[random.randint(0, len(self.NoneState)-1)]
    #        y = i//3
    #        x = i%3
    #        self.add_o(x, y)
    #        self.state[i] = 'o'
            
    def print_spitch(self, spitch):
        print(spitch)
        
    def click(self, event):
        if not self.gameover:
            x = event.x
            y = event.y
            if x in range (0, 101): x = 0
            elif x in range (101, 201): x = 1
            elif x in range (201, 301): x = 2
            if y in range (0, 101): y = 0
            elif y in range (101, 201): y = 1
            elif y in range (201, 301): y = 2
            
            if self.state[(x+3*y)] == None: 
                self.state[(x+3*y)] = self.player
                if self.player == 'x': 
                    self.add_x(x, y)
                    self.player = 'o'
                else: 
                    self.add_o(x, y)
                    self.player = 'x'
                
                a = self.get_winner()
                if a != None: 
                    self.print_spitch(a)
                    self.gameover = True
                    self.gamepause()
                elif self.state.count(None) == 1:
                    self.print_spitch('Игра окончена')
                    self.gameover = True
                    self.gamepause()
    
    def gamepause(self):
        text_object = self.create_text(150, 150, text='5', fill='green', font=('Arial', 200))
        self.update()
        time.sleep(1)
        for t in reversed(range(5)):
            self.itemconfig(text_object, text=str(t))
            self.update()
            time.sleep(1)
        self.delete("all")
        self.draw_lines()
        self.reinit()

    def get_winner(self):
        winner_x = ['x', 'x', 'x']
        winner_o = ['o', 'o', 'o']
        combination = [
            self.state[0:3], self.state[3:6], self.state[6:9], 
            self.state[0:7:3], self.state[1:8:3], self.state[2:9:3], 
            self.state[0:9:4], self.state[2:7:2]
        ]
        if winner_x in combination: 
            return 'x_win'
             
        elif winner_o in combination: 
            return 'o_win'
            
        elif None not in self.state:
            return 'draw'
                
        else:
            return None

window = tkinter.Tk()
game = TicTacToe(window)
game.draw_lines()
window.mainloop()