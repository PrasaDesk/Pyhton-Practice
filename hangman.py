import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200, borderwidth=0,
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

canvas.create_circle(100, 50, 20, fill="blue", outline="#DDD", width=4)

canvas.create_line(100, 50, 100, 120)

canvas.create_line(100, 75, 70, 90)    # Lh
canvas.create_line(100, 120, 70, 135)  # LL

canvas.create_line(100, 75, 140, 90)    # RH
canvas.create_line(100, 120, 140, 135)  # RL

root.wm_title("Circles and Arcs")
root.mainloop()
