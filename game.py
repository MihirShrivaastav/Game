from tkinter import *
from tkinter import messagebox

import time

word_list = ["Beautiful", "Java", "Library", "Technology", "Python",
             "TECHNOLOGY","BEAUTIFUL","JAVA",'LIBRARY','PYTHON']
score = 0;

window = Tk()

window.title("Find Words")
# window title bar name
window.geometry("940x900+0+0")
window.configure(bg='#9ED5C5')

# tkinter window size
def checkspells():
    global score
    total = "Score = " + str(score)
    label.configure(text=total)
    word = word_check.get();

    if word in word_list:
        flag = 1

        if flag == 1:
            score = score + len(word)
            total = "Score = " + str(score)
            label.configure(text=total)
            print(word)
    else:
        print("No Word")


def refresh():
    global score
    score = 0
    checkspells()

def add_word(text):
    global word_temp
    word_temp += text
    word_str.set(word_temp)


btn1 = Button(window, text="A", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'),  command=lambda: add_word("A"))
btn1.grid(column=1, row=1)
btn2 = Button(window, text="B", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'),  command=lambda: add_word("B"))
btn2.grid(column=2, row=1)
btn3 = Button(window, text="C", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("C"))
btn3.grid(column=3, row=1)
btn4 = Button(window, text="D", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("D"))
btn4.grid(column=4, row=1)
btn5 = Button(window, text="W", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("W"))
btn5.grid(column=5, row=1)
btn6 = Button(window, text="X", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("X"))
btn6.grid(column=6, row=1)
btn7 = Button(window, text="K", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("K"))
btn7.grid(column=7, row=1)
btn8 = Button(window, text="L", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("L"))
btn8.grid(column=8, row=1)
btn9 = Button(window, text="D", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("D"))
btn9.grid(column=9, row=1)
btn10 = Button(window, text="R", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("R"))
btn10.grid(column=10, row=1)
btn11 = Button(window, text="W", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("W"))
btn11.grid(column=11, row=1)
btn12 = Button(window, text="T", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("T"))
btn12.grid(column=12, row=1)

btn1 = Button(window, text="X", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("X"))
btn1.grid(column=1, row=2)
btn2 = Button(window, text="E", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("E"))
btn2.grid(column=2, row=2)
btn3 = Button(window, text="I", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("I"))
btn3.grid(column=3, row=2)
btn4 = Button(window, text="J", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("J"))
btn4.grid(column=4, row=2)
btn5 = Button(window, text="J", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("J"))
btn5.grid(column=5, row=2)
btn6 = Button(window, text="I", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("I"))
btn6.grid(column=6, row=2)
btn7 = Button(window, text="Y", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("Y"))
btn7.grid(column=7, row=2)
btn8 = Button(window, text="N", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("N"))
btn8.grid(column=8, row=2)
btn9 = Button(window, text="M", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("M"))
btn9.grid(column=9, row=2)
btn10 = Button(window, text="V", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("V"))
btn10.grid(column=10, row=2)
btn11 = Button(window, text="C", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("C"))
btn11.grid(column=11, row=2)
btn12 = Button(window, text="P", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("P"))
btn12.grid(column=12, row=2)

btn1 = Button(window, text="M", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("M"))
btn1.grid(column=1, row=3)
btn2 = Button(window, text="A", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("A"))
btn2.grid(column=2, row=3)
btn3 = Button(window, text="A", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("A"))
btn3.grid(column=3, row=3)
btn4 = Button(window, text="Q", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("Q"))
btn4.grid(column=4, row=3)
btn5 = Button(window, text="A", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("A"))
btn5.grid(column=5, row=3)
btn6 = Button(window, text="X", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("X"))
btn6.grid(column=6, row=3)
btn7 = Button(window, text="Z", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("Z"))
btn7.grid(column=7, row=3)
btn8 = Button(window, text="A", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("A"))
btn8.grid(column=8, row=3)
btn9 = Button(window, text="S", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("S"))
btn9.grid(column=9, row=3)
btn10 = Button(window, text="B", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("B"))
btn10.grid(column=10, row=3)
btn11 = Button(window, text="K", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("K"))
btn11.grid(column=11, row=3)
btn12 = Button(window, text="Y", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("Y"))
btn12.grid(column=12, row=3)

btn1 = Button(window, text="D", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("D"))
btn1.grid(column=1, row=4)
btn2 = Button(window, text="U", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("U"))
btn2.grid(column=2, row=4)
btn3 = Button(window, text="X", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("X"))
btn3.grid(column=3, row=4)
btn4 = Button(window, text="Z", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("Z"))
btn4.grid(column=4, row=4)
btn5 = Button(window, text="G", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("G"))
btn5.grid(column=5, row=4)
btn6 = Button(window, text="V", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("V"))
btn6.grid(column=6, row=4)
btn7 = Button(window, text="L", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("L"))
btn7.grid(column=7, row=4)
btn8 = Button(window, text="V", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("V"))
btn8.grid(column=8, row=4)
btn9 = Button(window, text="E", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("E"))
btn9.grid(column=9, row=4)
btn10 = Button(window, text="S", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("S"))
btn10.grid(column=10, row=4)
btn11 = Button(window, text="T", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("T"))
btn11.grid(column=11, row=4)
btn12 = Button(window, text="T", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("T"))
btn12.grid(column=12, row=4)

btn1 = Button(window, text="T", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("T"))
btn1.grid(column=1, row=5)
btn2 = Button(window, text="E", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("E"))
btn2.grid(column=2, row=5)
btn3 = Button(window, text="C", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("C"))
btn3.grid(column=3, row=5)
btn4 = Button(window, text="H", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("H"))
btn4.grid(column=4, row=5)
btn5 = Button(window, text="N", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("N"))
btn5.grid(column=5, row=5)
btn6 = Button(window, text="O", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("O"))
btn6.grid(column=6, row=5)
btn7 = Button(window, text="L", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("L"))
btn7.grid(column=7, row=5)
btn8 = Button(window, text="O", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("O"))
btn8.grid(column=8, row=5)
btn9 = Button(window, text="G", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("G"))
btn9.grid(column=9, row=5)
btn10 = Button(window, text="Y", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("Y"))
btn10.grid(column=10, row=5)
btn11 = Button(window, text="L", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("L"))
btn11.grid(column=11, row=5)
btn12 = Button(window, text="H", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("H"))
btn12.grid(column=12, row=5)

btn1 = Button(window, text="X", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("X"))
btn1.grid(column=1, row=6)
btn2 = Button(window, text="I", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("I"))
btn2.grid(column=2, row=6)
btn3 = Button(window, text="N", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("N"))
btn3.grid(column=3, row=6)
btn4 = Button(window, text="C", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("C"))
btn4.grid(column=4, row=6)
btn5 = Button(window, text="A", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("A"))
btn5.grid(column=5, row=6)
btn6 = Button(window, text="Q", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("Q"))
btn6.grid(column=6, row=6)
btn7 = Button(window, text="S", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("S"))
btn7.grid(column=7, row=6)
btn8 = Button(window, text="J", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("J"))
btn8.grid(column=8, row=6)
btn9 = Button(window, text="V", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("V"))
btn9.grid(column=9, row=6)
btn10 = Button(window, text="M", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("M"))
btn10.grid(column=10, row=6)
btn11 = Button(window, text="S", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("S"))
btn11.grid(column=11, row=6)
btn12 = Button(window, text="O", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("O"))
btn12.grid(column=12, row=6)

btn1 = Button(window, text="Z", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("Z"))
btn1.grid(column=1, row=7)
btn2 = Button(window, text="F", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("F"))
btn2.grid(column=2, row=7)
btn3 = Button(window, text="A", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("A"))
btn3.grid(column=3, row=7)
btn4 = Button(window, text="C", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("C"))
btn4.grid(column=4, row=7)
btn5 = Button(window, text="J", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("J"))
btn5.grid(column=5, row=7)
btn6 = Button(window, text="Z", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("Z"))
btn6.grid(column=6, row=7)
btn7 = Button(window, text="D", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("D"))
btn7.grid(column=7, row=7)
btn8 = Button(window, text="H", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("H"))
btn8.grid(column=8, row=7)
btn9 = Button(window, text="A", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("A"))
btn9.grid(column=9, row=7)
btn10 = Button(window, text="S", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("S"))
btn10.grid(column=10, row=7)
btn11 = Button(window, text="A", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("A"))
btn11.grid(column=11, row=7)
btn12 = Button(window, text="N", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("N"))
btn12.grid(column=12, row=7)

btn1 = Button(window, text="K", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("K"))
btn1.grid(column=1, row=8)
btn2 = Button(window, text="U", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("U"))
btn2.grid(column=2, row=8)
btn3 = Button(window, text="W", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("W"))
btn3.grid(column=3, row=8)
btn4 = Button(window, text="A", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("A"))
btn4.grid(column=4, row=8)
btn5 = Button(window, text="O", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("O"))
btn5.grid(column=5, row=8)
btn6 = Button(window, text="P", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("P"))
btn6.grid(column=6, row=8)
btn7 = Button(window, text="R", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("R"))
btn7.grid(column=7, row=8)
btn8 = Button(window, text="E", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("E"))
btn8.grid(column=8, row=8)
btn9 = Button(window, text="S", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("S"))
btn9.grid(column=9, row=8)
btn10 = Button(window, text="V", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("V"))
btn10.grid(column=10, row=8)
btn11 = Button(window, text="M", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("M"))
btn11.grid(column=11, row=8)
btn12 = Button(window, text="V", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("V"))
btn12.grid(column=12, row=8)

btn1 = Button(window, text="S", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("S"))
btn1.grid(column=1, row=9)
btn2 = Button(window, text="L", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("L"))
btn2.grid(column=2, row=9)
btn3 = Button(window, text="I", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("I"))
btn3.grid(column=3, row=9)
btn4 = Button(window, text="B", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("B"))
btn4.grid(column=4, row=9)
btn5 = Button(window, text="R", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("R"))
btn5.grid(column=5, row=9)
btn6 = Button(window, text="A", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("A"))
btn6.grid(column=6, row=9)
btn7 = Button(window, text="R", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("R"))
btn7.grid(column=7, row=9)
btn8 = Button(window, text="Y", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("Y"))
btn8.grid(column=8, row=9)
btn9 = Button(window, text="S", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("S"))
btn9.grid(column=9, row=9)
btn10 = Button(window, text="D", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("D"))
btn10.grid(column=10, row=9)
btn11 = Button(window, text="A", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("A"))
btn11.grid(column=11, row=9)
btn12 = Button(window, text="W", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("W"))
btn12.grid(column=12, row=9)

btn1 = Button(window, text="R", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("R"))
btn1.grid(column=1, row=10)
btn2 = Button(window, text="T", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("T"))
btn2.grid(column=2, row=10)
btn3 = Button(window, text="Y", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("Y"))
btn3.grid(column=3, row=10)
btn4 = Button(window, text="Y", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("Y"))
btn4.grid(column=4, row=10)
btn5 = Button(window, text="I", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("I"))
btn5.grid(column=5, row=10)
btn6 = Button(window, text="Z", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("Z"))
btn6.grid(column=6, row=10)
btn7 = Button(window, text="X", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("X"))
btn7.grid(column=7, row=10)
btn8 = Button(window, text="C", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("C"))
btn8.grid(column=8, row=10)
btn9 = Button(window, text="V", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("V"))
btn9.grid(column=9, row=10)
btn10 = Button(window, text="B", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("B"))
btn10.grid(column=10, row=10)
btn11 = Button(window, text="M", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("M"))
btn11.grid(column=11, row=10)
btn12 = Button(window, text="L", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("L"))
btn12.grid(column=12, row=10)

btn1 = Button(window, text="J", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("J"))
btn1.grid(column=1, row=11)
btn2 = Button(window, text="H", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("H"))
btn2.grid(column=2, row=11)
btn3 = Button(window, text="G", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("G"))
btn3.grid(column=3, row=11)
btn4 = Button(window, text="G", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("G"))
btn4.grid(column=4, row=11)
btn5 = Button(window, text="W", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("W"))
btn5.grid(column=5, row=11)
btn6 = Button(window, text="Q", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("Q"))
btn6.grid(column=6, row=11)
btn7 = Button(window, text="A", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("A"))
btn7.grid(column=7, row=11)
btn8 = Button(window, text="S", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("S"))
btn8.grid(column=8, row=11)
btn9 = Button(window, text="K", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("K"))
btn9.grid(column=9, row=11)
btn10 = Button(window, text="A", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("A"))
btn10.grid(column=10, row=11)
btn11 = Button(window, text="A", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("A"))
btn11.grid(column=11, row=11)
btn12 = Button(window, text="R", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("R"))
btn12.grid(column=12, row=11)

btn1 = Button(window, text="B", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("R"))
btn1.grid(column=1, row=12)
btn2 = Button(window, text="V", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("V"))
btn2.grid(column=2, row=12)
btn3 = Button(window, text="C", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("C"))
btn3.grid(column=3, row=12)
btn4 = Button(window, text="X", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("X"))
btn4.grid(column=4, row=12)
btn5 = Button(window, text="S", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("S"))
btn5.grid(column=5, row=12)
btn6 = Button(window, text="S", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("S"))
btn6.grid(column=6, row=12)
btn7 = Button(window, text="A", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("A"))
btn7.grid(column=7, row=12)
btn8 = Button(window, text="F", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("F"))
btn8.grid(column=8, row=12)
btn9 = Button(window, text="E", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("E"))
btn9.grid(column=9, row=12)
btn10 = Button(window, text="G", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("G"))
btn10.grid(column=10, row=12)
btn11 = Button(window, text="D", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("D"))
btn11.grid(column=11, row=12)
btn12 = Button(window, text="G", bg="#749F82", fg="black", width=4, height=1, font=('Times New Roman', '20'), command=lambda: add_word("G"))
btn12.grid(column=12, row=12)


word_temp = ""
word_str = StringVar()

word_check = Entry(window, width=20, bd=0, textvariable=word_str)
word_check.configure(highlightbackground="red", highlightcolor="red")
word_check.place(x=50, y=750)
word_check.focus()
btncheck = Button(window, text="OK", bg="#285430", fg="White", width=6, font=('Helvetica', '10'), command=checkspells)
btnrefresh = Button(window, text="Refresh", bg="#285430", fg="White", width=6, font=('Helvetica', '10'),
                    command=refresh)
btnexit = Button(window, text="Exit", bg="#285430", fg="White", width=6, font=('Helvetica', '10'), command=window.quit)
btnexit.place(x=550, y=750)
btncheck.place(x=100, y=800)
btnrefresh.place(x=550, y=800)
label = Label(window, text="Score = 0", bg="#9ED5C5")
label.place(x=300, y=750)
window.mainloop()