from tkinter import Entry, Button, Tk, Label

my_window = Tk()
my_window.title('Mile to Km converter')
my_window.config(padx=30, pady=50)
my_window.minsize(width=300, height=200)

input_user = Entry(width=10)
input_user.grid(row=0, column=1)

Label(text='Miles', font=('Arial', 15, 'italic')).grid(row=0, column=2)
Label(text='is equal to', font=('Arial', 15, 'italic')).grid(row=1, column=0)
Label(text='km', font=('Arial', 15, 'italic')).grid(row=1, column=2)
miles = Label(text='0', font=('Arial', 15, 'italic'))
miles.grid(row=1, column=1)


def calculate():
    try:
        miles['text'] = round(float(input_user.get()) * 1.60934, 2)
    except ValueError:
        print('Please write a correct number')


calculate_button = Button(text='calculate', font=('Arial', 12), command=calculate)
calculate_button.grid(row=2, column=1)

my_window.mainloop()
