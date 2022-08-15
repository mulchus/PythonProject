#version 15-08-22 with проверка на диагональный защищающий  ход
import tkinter
import random
import time


coord = [50, 150, 250]

class TicTacToe(tkinter.Canvas):  #разовая инициализация окна и констант 
    def __init__(self, window):
        self.winner_x = ['x', 'x', 'x']
        self.winner_o = ['o', 'o', 'o']
        self.reinit()
        self.window = window
        self.canvas = super().__init__(window, width=300, height=300)
        self.bind('<Button-1>', self.click)
        self.pack()

    def reinit(self):   #повторяющийся модуль при инициализации игрового поля 
        self.state = [None]*9 #список всех ячеек поля
        self.NoneState = [] #список пустых ячеек поля - вычисляется при хождении бота
        self.gameover = False   #признак конца игры для запрета кликов

    def gamepause(self):
        text_object = self.create_text(150, 150, text='3', fill='green', font=('Arial', 200))
        self.update()
        time.sleep(1)
        for t in reversed(range(1, 3)):
            self.itemconfig(text_object, text=str(t))
            self.update()
            time.sleep(1)
        self.delete("all")
        self.draw_lines()
        self.reinit()

    def draw_lines(self):   #рисуем линии на игровом поле   
         self.create_line(100, 0, 100, 300, fill='grey')
         self.create_line(200, 0, 200, 300, fill='grey')
         self.create_line(0, 100, 300, 100, fill='grey')
         self.create_line(0, 200, 300, 200, fill='grey')

    def add_o(self, column, row):   #модуль - по заранее вычисленным координатам рисуем "О" 
        r = 30
        column = coord[column]
        row = coord[row]
        self.create_oval(column-r, row-r, column+r, row+r, width=5, outline='red')

    def add_x(self, column, row):   #модуль - по заранее вычисленным координатам рисуем "Х"
        l = 30
        column = coord[column]
        row = coord[row]
        self.create_line(column-l, row-l, column+l, row+l, width=5, fill='blue')
        self.create_line(column-l, row+l, column+l, row-l, width=5, fill='blue')

    def bot_move(self): #модуль хождения бота
        new_coord = None   #инициализация итоговой координаты бота из числа 1я-8я клетка  
        combination = [     #закладываем срезы по вертикали, горизонтали и диагонали в память
            self.state[0:3], self.state[3:6], self.state[6:9], 
            self.state[0:7:3], self.state[1:8:3], self.state[2:9:3], 
            self.state[0:9:4], self.state[2:7:2]
        ]
        #реализуем проверку на выйгрышный ход
        #по наличию в срезах значений из двух О и None    
        for i in range(8):  #проверяем срезы на выйгрышные комбинации
            #print(str(combination[i]))
            if (combination[i] == ['o', None, 'o']
            or combination[i] == ['o', 'o', None] 
            or combination[i] == [None, 'o', 'o']): 
                win = combination[i].index(None)
                #print(f'win = {win} выйгрышная комбинация № {i}')
                if i in range(3):   #если выйгрышно в горизонталях - вычисляем new_coord
                    new_coord = i*3+win
                    #print(f'Есть место {new_coord}')
                elif i in range(3, 6):  #если выйгрышно в вертикалях - вычисляем new_coord
                    new_coord = win*3+(i-3)
                    #print(f'Есть место {new_coord}')
                elif i == 6:  #если выйгрышно в прямой диагонали - вычисляем new_coord
                    new_coord = win*4
                    #print(f'Есть место {new_coord}')
                elif i == 7:  #если выйгрышно в обратной диагонали - вычисляем new_coord
                    new_coord = win*2+2
                    #print(f'Есть место {new_coord}')   
        if new_coord is None:
            for i in range(8):  #проверяем срезы на опасные комбинации
                #print(str(combination[i]))
                if (combination[i] == ['x', None, 'x']
                or combination[i] == ['x', 'x', None] 
                or combination[i] == [None, 'x', 'x']): 
                    empty = combination[i].index(None)
                    #print(f'empty = {empty} комбинация № {i}')
                    if i in range(3):   #если опасно в горизонталях - вычисляем new_coord
                        new_coord = i*3+empty
                        #print(f'Есть место {new_coord}')
                    elif i in range(3, 6):  #если опасно в вертикалях - вычисляем new_coord
                        new_coord = empty*3+(i-3)
                        #print(f'Есть место {new_coord}')
                    elif i == 6:  #если опасно в прямой диагонали - вычисляем new_coord
                        new_coord = empty*4
                        #print(f'Есть место {new_coord}')
                    elif i == 7:  #если опасно в обратной диагонали - вычисляем new_coord
                        new_coord = empty*2+2
                        #print(f'Есть место {new_coord}')    
            if new_coord is None:   #если не найдено опасное место (new_coord будет None) 

                if self.state[4] is None:   #проверяем свободен ли центр поля
                    new_coord = 4           #если ДА - ходим туда
                else:                       #иначе
                    for i in range(6, 8):  #проверяем срезы на пустые комбинации по диагонали
                        #print(str(combination[i]))
                        if (combination[i] == [None, 'x', None]
                        or combination[i] == ['x', None, None]
                        or combination[i] == [None, None, 'x']):
                            empty = combination[i].index(None)
                            print(f'empty = {empty} комбинация № {i}')
                            if i == 6:  #если опасно в прямой диагонали - вычисляем new_coord
                                new_coord = empty*4
                        #print(f'Есть место {new_coord}')
                            elif i == 7:  #если опасно в обратной диагонали - вычисляем new_coord
                                new_coord = empty*2+2
                        #print(f'Есть место {new_coord}')
                if new_coord is None:  #иначе
                    self.NoneState = []     #реализуем выбор случайной координаты
                    for i in range(9):
                        if self.state[i] is None:  #набираем список номеров пустых ячеек 
                            self.NoneState.append(i)    #в список NoneState
                    if len(self.NoneState) > 0: #и из собранного списка случайно выбираем координату
                        new_coord = random.choice(self.NoneState)                 
                    #print(f'А это место рандом = {new_coord}')
            #print(f'Ставим О на {new_coord}')
        y = new_coord//3    #вычисляем по номеру ячейки столбец
        x = new_coord%3     #и строку
        self.add_o(x, y)    #и рисуем "О"
        self.state[new_coord] = 'o'  #в список ячеек вносим на свою позицию 'о'     


    def print_spitch(self, spitch): #модуль вывода сообщений
        print(spitch)

    def click(self, event): #модуль хода игрока
        if not self.gameover: #проверка на признак конца игры
            x = event.x #получаем координаты клика в пикселях
            y = event.y
            x = x//100  #и вычисляем номер сроки х
            y = y//100  #и номер столбца y
            if self.state[(x+3*y)] is None: #проверка, свободна ли ячейка
                self.state[(x+3*y)] = 'x'   #если да - отметка что теперь занята
                self.add_x(x, y)    #и рисуем Х

                a = self.get_winner()   #проверяем на возможный факт победы игрока
                if a == 'x_win':    #если вернуло 'x_win'
                    self.print_spitch('Вы победили!!!') #информируем на экране
                    self.gameover = True    #и ставим признак конца игры для игнорирования кликов 
                    self.gamepause()

                elif None in self.state:    #иначе если есть пустоты в списке всех ячеек поля
                    self.bot_move()     #запускаем модуль хождения бота

                    a = self.get_winner() #проверяем на возможный факт победы бота
                    if a is not None: #если вернуло что то
                        self.print_spitch(a) #выводим на экран что вернуло
                        self.gameover = True    #и ставим признак конца игры для игнорирования кликов
                        self.gamepause()    #пауза и модуль обратного счета 

                    elif self.state.count(None) == 1:   #иначе если осталась одна клетка
                        self.print_spitch('Ничья')  #игра окончена
                        self.gameover = True
                        self.gamepause()

                else:   #а если пустот в списке всех ячеек поля больше нет (проверяется в модуле get_winner)
                    self.print_spitch(a) #должно отобразиться сообщение 'draw'
                    self.gameover = True   #и ставим признак конца игры для игнорирования кликов 
                    self.gamepause()

    def get_winner(self):   #модуль проверки победителя
        line = None
        self.line_pul = [
            [0, 0, 2, 0], [0, 1, 2, 1], [0, 2, 2, 2],
            [0, 0, 0, 2], [1, 0, 1, 2], [2, 0, 2, 2],
            [0, 0, 2, 2], [2, 0, 0, 2]
        ] 
        self.combination = [     #закладываем текущие срезы по вертикали, горизонтали и диагонали в память
            self.state[0:3], self.state[3:6], self.state[6:9], 
            self.state[0:7:3], self.state[1:8:3], self.state[2:9:3], 
            self.state[0:9:4], self.state[2:7:2]
        ]
        if self.winner_x in self.combination: #если победная комбинация игрока есть в списке срезов
            self.line = self.combination.index(self.winner_x) #вычисляем координаты линии перечеркивания
            self.winline()
            return 'x_win'  #возвращаем 'x_win'

        elif self.winner_o in self.combination: #если победная комбинация бота есть в списке срезов
            self.line = self.combination.index(self.winner_o) #вычисляем координаты линии перечеркивания
            self.winline()
            return 'Победил БОТ :)'  #возвращаем 'o_win'

        elif None not in self.state: #иначе если нет пустот в списке всех ячеек поля
            return 'Свободное место закончилось...'   #возвращаем 'draw'
        else:   #или ничего не возвращаем
            return None

    def winline(self):  #модуль вычисляем координаты линии перечеркивания
        x1 = coord[self.line_pul[self.line][0]]
        y1 = coord[self.line_pul[self.line][1]]
        x2 = coord[self.line_pul[self.line][2]]
        y2 = coord[self.line_pul[self.line][3]]
        self.create_line(x1, y1, x2, y2, width=10, fill='yellow')
        self.update()

window = tkinter.Tk()
game = TicTacToe(window)
game.draw_lines()
#ручная проверка 
#game.state =  [None, None, None, None, 'x', None, 'o', None, 'x']
#game.bot_move()
#game.state = ['o', 'x', 'o', 'o', 'o', 'x', 'x', 'o', 'x']
#print(game.get_winner())
window.mainloop()