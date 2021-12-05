from tkinter import Button, Tk, Frame, Entry, END
import tkinter
from uncertainties import ufloat_fromstr

ventana = Tk()
ventana.geometry('350x280')
ventana.config(bg="white")
ventana.resizable(0, 0)
ventana.title('Calculadora con incertezas')


class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self["background"] = self["activebackground"]

    def on_leave(self, e):
        self["background"] = self.defaultBackground


def obtener(dato):
    op = dato
    if str(op) == "-" or str(op) == "+" or str(op) == "/" or str(op) == "*" or str(op) == "^":
        ope.delete(0, END)
        ope.insert(0, dato)
    else:
        if str(num1.focus_get()) == '.!frame.!entry':
            num1.insert(len(num1.get()), dato)
        else:
            num2.insert(len(num2.get()), dato)


def operacion():
    try:
        n1 = ufloat_fromstr(num1.get())
        result = 'null'
        if ope.get() == '-':
            result = n1 - ufloat_fromstr(num2.get())
        elif ope.get() == '+':
            result = n1 + ufloat_fromstr(num2.get())
        elif ope.get() == '/':
            result = n1 / ufloat_fromstr(num2.get())
        elif ope.get() == '*':
            result = n1 * ufloat_fromstr(num2.get())
        elif ope.get() == '^':
            result = n1 ** ufloat_fromstr(num2.get())
        print(result)
        num1.delete(0, END)
        num2.delete(0, END)
        num1.insert(0, result)

    except:
        result = 'ERROR'
        num1.delete(0, END)
        num2.delete(0, END)
        num1.insert(0, result)


def borrar_uno():
    if str(num1.focus_get()) == '.!frame.!entry':

        num1.delete(len(num1.get())-1, tkinter.END)

    elif str(num2.focus_get()) == '.!frame.!entry3':

        num2.delete(len(num2.get())-1, tkinter.END)


def borrar_todo():
    num1.delete(0, END)
    num2.delete(0, END)
    ope.delete(0, END)


CNButton_Stand = '#999AB8'
CNButton_hover = '#4f4f60'

COButton_Stand = '#77a4e9'
COButton_hover = '#1e5fc0'

CODButton_Stand = '#e9b374'
CODButton_hover = '#ca7511'

COLButton_Stand = '#e97474'
COLButton_hover = '#c01e1e'

COCButton_Stand = '#77d8a0'
COCButton_hover = '#55ab09'

# fila 0

frame = Frame(ventana, relief="raised")
frame.grid(column=0, row=0, padx=6, pady=3)

num1 = Entry(frame, bg='#9EF8E8', width=9, relief='groove',
             font='Montserrat 16', justif='right')
num1.grid(columnspan=2, column=0, row=0, pady=0, padx=0, ipadx=0, ipady=5)

ope = Entry(frame, width=1,
            font='Montserrat 16', justif='right')
ope.grid(column=2, row=0, pady=0, padx=0, ipadx=0, ipady=1)

num2 = Entry(frame, bg='#9EF8E8', width=9, relief='groove',
             font='Montserrat 16', justif='right')
num2.grid(columnspan=2, column=3, row=0, pady=0, padx=0, ipadx=5, ipady=5)


# fila 1
Button1 = HoverButton(frame, text="1", borderwidth=2, height=2, width=5, font=('Comic sens MC', 12, 'bold'),
                      relief="raised", activebackground=CNButton_hover, bg=CNButton_Stand,  anchor="center", command=lambda: obtener(1))
Button1.grid(column=0, row=1, pady=1, padx=3)
Button2 = HoverButton(frame, text="2", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                      relief="raised", activebackground=CNButton_hover, bg=CNButton_Stand, anchor="center", command=lambda: obtener(2))
Button2.grid(column=1, row=1, pady=1, padx=1)

Button3 = HoverButton(frame, text="3", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                      relief="raised", activebackground=CNButton_hover, bg=CNButton_Stand, anchor="center", command=lambda: obtener(3))
Button3.grid(column=2, row=1, pady=1, padx=1)

Button_borrar = HoverButton(frame, text="C", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                            relief="raised", activebackground=COLButton_hover, bg=COLButton_Stand, anchor="center", command=lambda: borrar_todo())
Button_borrar.grid(column=3, row=1, pady=2, padx=2)

Button_backspace = HoverButton(frame, text="⌫", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                               relief="raised", activebackground=CODButton_hover, bg=CODButton_Stand,  anchor="center", command=lambda: borrar_uno())
Button_backspace.grid(column=4, row=1, pady=2, padx=2)

# fila 2
Button4 = HoverButton(frame, text="4", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                      relief="raised", activebackground=CNButton_hover, bg=CNButton_Stand, anchor="center", command=lambda: obtener(4))
Button4.grid(column=0, row=2, pady=1, padx=1)
Button5 = HoverButton(frame, text="5", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                      relief="raised", activebackground=CNButton_hover, bg=CNButton_Stand, anchor="center", command=lambda: obtener(5))
Button5.grid(column=1, row=2, pady=1, padx=1)
Button6 = HoverButton(frame, text="6", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                      relief="raised", activebackground=CNButton_hover, bg=CNButton_Stand,  anchor="center", command=lambda: obtener(6))
Button6.grid(column=2, row=2, pady=1, padx=1)

Button_por = HoverButton(frame, text="x", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                         relief="raised", activebackground=COButton_hover, bg=COButton_Stand,  anchor="center", command=lambda: obtener('*'))
Button_por.grid(column=3, row=2, pady=2, padx=2)

Button_entre = HoverButton(frame, text="÷", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                           relief="raised", activebackground=COButton_hover, bg=COButton_Stand,  anchor="center", command=lambda: obtener('/'))
Button_entre.grid(column=4, row=2, pady=1, padx=1)

# fila 3
Button7 = HoverButton(frame, text="7", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                      relief="raised", activebackground=CNButton_hover, bg=CNButton_Stand,  anchor="center", command=lambda: obtener(7))
Button7.grid(column=0, row=3, pady=1, padx=1)
Button8 = HoverButton(frame, text="8", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                      relief="raised", activebackground=CNButton_hover, bg=CNButton_Stand, anchor="center", command=lambda: obtener(8))
Button8.grid(column=1, row=3, pady=1, padx=1)
Button9 = HoverButton(frame, text="9", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                      relief="raised", activebackground=CNButton_hover, bg=CNButton_Stand,  anchor="center", command=lambda: obtener(9))
Button9.grid(column=2, row=3, pady=1, padx=1)

Button_mas = HoverButton(frame, text="+", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                         relief="raised", activebackground=COButton_hover, bg=COButton_Stand,  anchor="center", command=lambda: obtener('+'))
Button_mas.grid(column=3, row=3, pady=2, padx=2)

Button_menos = HoverButton(frame, text="-", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                           relief="raised", activebackground=COButton_hover, bg=COButton_Stand,  anchor="center", command=lambda: obtener('-'))
Button_menos.grid(column=4, row=3, pady=2, padx=2)


# fila 4

Button_pm = HoverButton(frame, text=u"\u00B1", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                        relief="raised", activebackground=COButton_hover, bg=COButton_Stand,  anchor="center", command=lambda: obtener(u"\u00B1"))
Button_pm.grid(column=0, row=4, pady=2, padx=2)

Button0 = HoverButton(frame, text="0", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                      relief="raised", activebackground=CNButton_hover, bg=CNButton_Stand,  anchor="center", command=lambda: obtener(0))
Button0.grid(column=1, row=4, pady=1, padx=1)

Button_punto = HoverButton(frame, text=".", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                           relief="raised", activebackground=CNButton_hover, bg=CNButton_Stand, anchor="center", command=lambda: obtener('.'))
Button_punto.grid(column=2, row=4, pady=1, padx=1)

Button_pow = HoverButton(frame, text="^", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                         relief="raised", activebackground=COButton_hover, bg=COButton_Stand,  anchor="center", command=lambda: obtener('^'))
Button_pow.grid(column=3, row=4, pady=1, padx=1)

Button_igual = HoverButton(frame, text="=", height=2, width=5, font=('Comic sens MC', 12, 'bold'), borderwidth=2,
                           relief="raised", activebackground=COCButton_hover, bg=COCButton_Stand, anchor="center", command=lambda: operacion())
Button_igual.grid(column=4, row=4, pady=1, padx=1)

ventana.mainloop()
