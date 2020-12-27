from tkinter import *

root = Tk()

img1 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Documents\002-1.png")
img2 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Documents\003-2.png")
img3 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Documents\004-3.png")
img4 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Documents\008-4.png")
img5 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Documents\009-5.png")
img6 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Documents\010-6.png")
img7 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Documents\007-7.png")
img8 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Documents\006-8.png")
img9 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Documents\005-9.png")
img0 = PhotoImage(file=r"C:\Users\AZAR\Downloads\Documents\001-0.png")
imgplus = PhotoImage(file=r"C:\Users\AZAR\Downloads\Documents\011-plus.png")
imgmoih = PhotoImage(file=r"C:\Users\AZAR\Downloads\Documents\013-minus.png")
imgdarb = PhotoImage(file=r"C:\Users\AZAR\Downloads\Documents\014-asterisk.png")
img9isma = PhotoImage(file=r"C:\Users\AZAR\Downloads\Documents\012-division.png")
imgfasila = PhotoImage(file=r"C:\Users\AZAR\Downloads\Documents\001-ball.png")
imgclear = PhotoImage(file=r"C:\Users\AZAR\Downloads\Documents\016-c.png")
imgequal = PhotoImage(file=r"C:\Users\AZAR\Downloads\Documents\015-equal.png")
root.geometry("400x500")
root.columnconfigure([0, 1, 2, 3, 4], weight=5)
root.rowconfigure([0, 1, 2, 3, 4], weight=4)



#def
def insert(id):
    if id == "clear":
        En.delete(0, END)
    elif id != "=":
        En.insert("end", id)

    else:
        operation = eval(En.get())
        En.delete(0,END)
        En.insert(0, "{}".format(operation))
def button(text, img,bg, rw, clmn):
    Button(root, image=img, bg=bg, text=text, command=lambda:insert(text)).grid(row=rw, column=clmn, sticky=N+S+W+E)
def buttonspan2(text, img,bg, rw, clmn):
    Button(root, text=text, image=img, bg=bg, command=lambda:insert(text)).grid(row=rw, column=clmn,columnspan=2, sticky=N+S+W+E)



En = Entry(root, background="#E7FDC0", font="arial 30")
En.grid(row=0, column=0, columnspan=5, ipadx=4, ipady=8)

button("7", img7, '#DAF7A6', 1, 0)
button("8", img8, '#DAF7A6', 1, 1)
button("9", img9, '#DAF7A6', 1, 2)
buttonspan2("clear", imgclear, '#DAF7A6', 1, 3)

button("4", img4, '#CBEF8B', 2, 0)
button("5", img5, '#CBEF8B', 2, 1)
button("6", img6, '#CBEF8B', 2, 2)
button("-", imgmoih, '#CBEF8B', 2, 3)
button("*", imgdarb, '#CBEF8B', 2, 4)

button("1", img1, '#ACD563', 3, 0)
button("2", img2, '#ACD563', 3, 1)
button("3", img3, '#ACD563', 3, 2)
button("+", imgplus, '#ACD563', 3, 3)
button("/", img9isma, '#ACD563', 3, 4)

button(".", imgfasila, '#92B84E', 4, 0)
buttonspan2("0", img0, '#92B84E', 4, 1)
buttonspan2("=", imgequal, '#92B84E', 4, 3)


root.mainloop()
