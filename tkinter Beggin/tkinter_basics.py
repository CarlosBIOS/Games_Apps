import tkinter

window = tkinter.Tk()
window.title('My first Gui Program')
# window.geometry('640x480')
window.config(padx=20, pady=20)
window.minsize(width=500, height=300)
window.maxsize(width=640, height=480)

my_label = tkinter.Label(text='I am a Label', font=('Arial', 24, 'italic'))
my_label.grid(row=0, column=0)
# my_label.pack()  # Basicamente, coloca no window automaticamente e centraliza-o na parte de cima
# my_label.pack(side='left')  # Basicamente, coloca no window automaticamente e centraliza-o na parte da esquerda
# my_label.pack(side='bottom')  # Basicamente, coloca no window automaticamente e centraliza-o na parte debaixo
# my_label.pack(expand=True)  # Basicamente, coloca no window automaticamente e centraliza-o na parte central
# my_label.place(x=100, y=100)


def button_clicked():
    my_label['text'] = input_user.get()


choice_button = tkinter.Button(text='choice', font=('Arial', 12), command=button_clicked)
# choice_button.pack()
choice_button.grid(row=1, column=1)

new_button = tkinter.Button(text='new Button', font=('Arial', 12), command=button_clicked)
new_button.grid(row=0, column=2)

input_user = tkinter.Entry(width=10)
# input_user.pack()
input_user.grid(row=2, column=3)

window.mainloop()
