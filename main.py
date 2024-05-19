from tkinter import *
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ---------------------------- READ DATA ------------------------------- #

try:
    data = pd.read_csv("data/french_words.csv") # Reads the original file
except FileNotFoundError:
    original_Data = pd.read__csv("data/french_words.csv")
    to_learn = original_Data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    

# ---------------------------- CARD FUNCTION ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) # Cancel the previous flip timer when on a new word
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, flip_card) # creating a new timer to flip the card

def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back)

def is_known():
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



# Loading images
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# Setting up the canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
r_btn = Button(image=right_image, highlightthickness=0, command=is_known)
r_btn.grid(row=1, column=1)
wrng_btn = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrng_btn.grid(row=1, column=0)

# Initialize the first card and flip timer
flip_timer = window.after(3000, flip_card)
next_card() # Displaying the first card


window.mainloop()

