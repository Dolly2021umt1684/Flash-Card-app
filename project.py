from tkinter import *
import random
import pandas



BACKGROUND_COLOR = "#B1DDC6"
flip_timer=None
current_card={}


#________________________________Creating new Flash Cards_________________________#

# reading data from csv
try:
    data= pandas.read_csv('words_to_learn.csv')

except FileNotFoundError:
    data=pandas.read_csv('french_words.csv')
    dict = data.to_dict(orient='records')
else:
    dict=data.to_dict(orient='records')
# this is dictionary in the form [{french_word: english_word}, {french_word2: english_word2}, {french_word3: english_word3}]
# print(dict)


def get_ans(answer):
     canvas.itemconfig(canvas_image,image=back_image_path)
     canvas.itemconfig(card_title,text='English',font=("Ariel", 40, 'italic'),fill='white')
     canvas.itemconfig(card_text,text=answer,font=("Ariel", 60, 'bold'),fill='white')



def change_word():
    global flip_timer,current_card
    window.after_cancel(flip_timer)
    current_card=random.choices(dict)[0]
    french_word=current_card["French"]
    english_word=current_card['English']
    canvas.itemconfig(canvas_image,image=photo_path)
    canvas.itemconfig(card_text, text=french_word,fill='black')
    canvas.itemconfig(card_title, text='French',fill='black')
    flip_timer=window.after(3000,get_ans,english_word)

def right_change_word():
    global flip_timer,current_card
    window.after_cancel(flip_timer)
    current_card=random.choices(dict)[0]
    french_word=current_card["French"]
    english_word=current_card['English']
    canvas.itemconfig(canvas_image,image=photo_path)
    canvas.itemconfig(card_text, text=french_word,fill='black')
    canvas.itemconfig(card_title, text='French',fill='black')
    flip_timer=window.after(3000,get_ans,english_word)
    is_known()
def is_known():
    global current_card
    dict.remove(current_card)
    data=pandas.DataFrame(dict)
    data.to_csv('words_to_learn.csv',index=False)



#____________________________________UI STEUP_____________________________________#

window = Tk()
window.title("Flashy")
window.configure(bg=BACKGROUND_COLOR,padx=50,pady=50)

canvas=Canvas(height=526,width=800,highlightthickness=0,bg=BACKGROUND_COLOR)
photo_path=PhotoImage(file='card_front.png')
canvas_image=canvas.create_image(400,263,image=photo_path)
card_title=canvas.create_text(400, 150, text='Title', font=("Ariel", 40, 'italic'))
card_text=canvas.create_text(400, 263, text='Word', font=("Ariel", 60, 'bold'))
canvas.grid_configure(row=0 , column=0,columnspan=2)

back_image_path=PhotoImage(file='card_back.png')

right_image_path=PhotoImage(file='right.png')
right_button= Button(image=right_image_path,bg=BACKGROUND_COLOR,highlightthickness=0,command=right_change_word)
right_button.grid_configure(row=1,column=1)

wrong_image_path=PhotoImage(file='wrong.png')
wrong_button=Button(image=wrong_image_path,bg=BACKGROUND_COLOR,highlightthickness=0,command=change_word)
wrong_button.grid(row=1,column=0)

flip_timer = window.after(10,get_ans,'word')




window.mainloop()