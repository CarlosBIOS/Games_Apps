import tkinter as tk
import pandas
import glob


def count_time(count):
    if count > 0:
        window.after(1000, count_time, count - 1)
    else:
        canvas.itemconfig(image1, image=image_object[0])
        canvas.itemconfig(text1, text='English')
        canvas.itemconfig(text2, text=data[0]['English'])
        data.pop(0)


def right_wrong_button():
    if data:
        return
    canvas.itemconfig(image1, image=image_object[1])
    canvas.itemconfig(text1, text='French')
    canvas.itemconfig(text2, text=data[0]['French'])
    count_time(5)


# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
images: list = glob.glob('Images/*.png')
# ['Images\\card_back.png', 'Images\\card_front.png', 'Images\\right.png', 'Images\\wrong.png']

window = tk.Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

image_object: list = [tk.PhotoImage(file=element) for element in images]

button_wrong = tk.Button(image=image_object[2], highlightthickness=0, bg=BACKGROUND_COLOR, border=0,
                         command=right_wrong_button)
button_wrong.grid(row=1, column=0, sticky='s')

button_right = tk.Button(image=image_object[3], highlightthickness=0, bg=BACKGROUND_COLOR, border=0,
                         command=right_wrong_button)
button_right.grid(row=1, column=1, sticky='s')

data: list = pandas.read_csv('data/french_words.csv').to_dict(orient='records')  #
# [{column -> value}, … , {column -> value}]!!!!
print(data)

canvas = tk.Canvas(width=800, height=525, highlightthickness=False, bg=BACKGROUND_COLOR)
image1 = canvas.create_image(400, 263, image=image_object[1])
text1 = canvas.create_text(400, 150, text='French', fill='black', font=('Arial', 40, 'italic'))
text2 = canvas.create_text(400, 263, text=data[0]['French'], fill='black', font=('Arial', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

count_time(5)

window.mainloop()
