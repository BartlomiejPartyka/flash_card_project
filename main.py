from tkinter import *
import pandas as p
from random import choice

words_df = p.DataFrame()
words_to_learn = {}
FOREIGN_LANGUAGE = ''
KNOWN_LANGUAGE = ''
WAITING_TIME = 3
word_dict = {}
BACKGROUND_COLOR = "#B1DDC6"


def load_data():
    global words_df, words_to_learn, FOREIGN_LANGUAGE, KNOWN_LANGUAGE
    try:
        words_df = p.read_csv('.\\data\\to_learn.csv')
        print('File found!')
    except FileNotFoundError:
        words_df = p.read_csv('.\\data\\french_words.csv')
    finally:
        words_to_learn = words_df.to_dict(orient='records')
        FOREIGN_LANGUAGE = words_df.columns.values.tolist()[0].title()
        KNOWN_LANGUAGE = words_df.columns.values.tolist()[1].title()


def word_known():
    words_to_learn.remove(word_dict)
    to_learn_df = p.DataFrame.from_dict(words_to_learn)
    to_learn_df.to_csv('.\\data\\to_learn.csv', index=False)
    choose_word()


def choose_word():
    global words_to_learn, word_dict, flip_timer
    window.after_cancel(flip_timer)
    word_dict = choice(words_to_learn)
    canvas.itemconfig(language_l, text=FOREIGN_LANGUAGE, fill='black')
    canvas.itemconfig(word_l, text=word_dict[FOREIGN_LANGUAGE], fill='black')
    canvas.itemconfig(CANVAS_IMAGE, image=FC_FRONT)
    flip_timer = window.after(3000, func=update_card)


def update_card():
    global word_dict
    canvas.itemconfig(language_l, text=KNOWN_LANGUAGE, fill='white')
    canvas.itemconfig(word_l, text=word_dict[KNOWN_LANGUAGE], fill='white')
    canvas.itemconfig(CANVAS_IMAGE, image=FC_BACK)


load_data()
window = Tk()
window.title('Password Manager')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=choose_word)

FC_FRONT = PhotoImage(file='.\\images\\card_front.png')
FC_BACK = PhotoImage(file='.\\images\\card_back.png')
RIGHT = PhotoImage(file='.\\images\\right.png')
WRONG = PhotoImage(file='.\\images\\wrong.png')

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
CANVAS_IMAGE = canvas.create_image(400, 263, image=FC_FRONT)
canvas.grid(row=0, column=0, columnspan=2)

right_btn = Button(image=RIGHT, command=word_known)
right_btn.grid(row=1, column=0)

wrong_btn = Button(image=WRONG, command=choose_word)
wrong_btn.grid(row=1, column=1)

language_l = canvas.create_text(400, 150, text='Title', fill='black', font=('Arial', 40, 'italic'))
word_l = canvas.create_text(400, 263, text='Title', fill='black', font=('Arial', 60, 'bold'))

window.mainloop()
