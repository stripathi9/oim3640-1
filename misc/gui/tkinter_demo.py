from tkinter import *


def demo():
    window = Tk()

    window.title("Welcome to my first app")
    window.geometry('350x200')

    txt = Entry(window, width=10)
    txt.grid(column=1, row=0)

    lbl = Label(window, text="Hello", font=("Arial Bold", 20))
    lbl.grid(column=0, row=0)

    def clicked():
        lbl.configure(text=txt.get() + ", How are you?")

    btn = Button(window, text="Click Me", command=clicked)
    btn.grid(column=0, row=1)

    window.mainloop()


if __name__ == "__main__":
    demo()
