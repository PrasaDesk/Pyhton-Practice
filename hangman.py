import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=500, borderwidth=0,
                   highlightthickness=0, bg="white")
canvas.grid()


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)


tk.Canvas.create_circle = _create_circle


def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)


tk.Canvas.create_circle_arc = _create_circle_arc


x = [1]


def addG():
    print("hi")
    if(len(x) == 1):
        canvas.create_circle(100, 50, 20, fill="blue", outline="#DDD", width=4)
    elif(len(x) == 2):
        canvas.create_line(100, 50, 100, 120)
    elif(len(x) == 3):
        canvas.create_line(100, 75, 70, 90)    # Lh
    elif(len(x) == 4):
        canvas.create_line(100, 75, 140, 90)    # RH
    elif(len(x) == 5):
        canvas.create_line(100, 120, 70, 135)  # LL
    elif(len(x) == 6):
        canvas.create_line(100, 120, 140, 135)  # RL
    x.append(3)


tk.Button(root, text="Submit", command=addG)


root.wm_title("Circles and Arcs")
root.mainloop()
