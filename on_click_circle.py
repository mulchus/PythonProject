import tkinter
import random
# ������� ����
window = tkinter.Tk()
# ������� ����� � ��������� ��� � ����
canvas = tkinter.Canvas(window, width=600, height=600)
canvas.pack()
colors=['red', 'green', 'gold', 'blue', 'white', 'black', 'yellow']
#x=150
#y=100
last_color = ''

def my_click(event):
    global last_color
    color = colors[random.randint(0, 5)]
    #����� �������� �� ������������� ����� � ��� ������� ���� true
    if color == last_color:
        if colors.index(color) == len(colors)-1:
            color = colors[0]
        else: color = colors[colors.index(color)+1]
    r = random.randint(10, 50)
    x0 = event.x - r
    y0 = event.y - r
    x1 = event.x + r
    y1 = event.y + r
    canvas.create_oval(x0, y0, x1, y1, outline=color)
    print(last_color, x0, y0, x1, y1, color)
    last_color = color
    canvas.update()
    
    #print(f'���� �� ������ � ����� x={event.x}, y={event.y}')

canvas.bind('<Button-1>', my_click)
window.mainloop()