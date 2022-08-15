import tkinter
import time
import random
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=400, height=400)
canvas.pack()
colors = ['red', 'green', 'gold', 'blue', 'white']
circles = []
for i in range(0, 5):
    x = random.randint(35, 365)
    y = random.randint(35, 365)
    r = random.randint(5, 35)
    key = canvas.create_oval(x-r, y-r, x+r, y+r, fill = random.choice(colors))
    dx = random.randint(-10, 10)
    dy = random.randint(-10, 10)
    data = {'dx': dx, 'dy': dy, 'id': key}
    circles.append(data)
print(circles)

while True:
    for circle in circles:
        x0, y0, x1, y1 = canvas.coords(circle['id'])
        if x0 + circle['dx'] <= 0: circle['dx'] *= -1
        if y0 + circle['dy'] <= 0: circle['dy'] *= -1
        if x1 + circle['dx'] >= 400: circle['dx'] *= -1
        if y1 + circle['dx'] >= 400: circle['dy'] *= -1
        canvas.move(circle['id'], circle['dx'], circle['dy'])
    
    canvas.update()
    time.sleep(0.05)
window.mainloop()
