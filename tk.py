import tkinter

top = tkinter.Tk()


def helloCallBack():
    print("hello")


en = tkinter.Entry(top)

B = tkinter.Button(top, text="Hello", command=helloCallBack)

B.pack()
top.mainloop()
