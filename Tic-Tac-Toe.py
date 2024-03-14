#Tic Tac Toe
#A simple app that allows the user to play tic tac toe against the computer where the computer auto-generates possible movies in order to win against the user.


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

root = Tk()

#FUNCTIONS: printboard, boardcopy, insertletter, spaceisFree, define letter, isWinner, playerMove, compMove, selectrandom , boardfull, mains


#printboard()
def printboard():

    global buttons

    root.title("TIC TAC TOE GAME")
    root.geometry("342x395+1000+100")
    root.resizable(False, False)

    b7 = Button(root, width=14, text=" ", height=7, command=lambda: [define_button(7), playerMove()])
    b7.place(x=0, y=30)

    b8 = Button(root, width=14, text=" ", height=7, command=lambda: [define_button(8), playerMove()])
    b8.place(x=117, y=30)

    b9 = Button(root, width=14, text=" ", height=7, command=lambda: [define_button(9), playerMove()])
    b9.place(x=234, y=30)

    b4 = Button(root, width=14, text=" ", height=7, command=lambda: [define_button(4), playerMove()])
    b4.place(x=0, y=155)

    b5 = Button(root, width=14, text=" ", height=7, command=lambda: [define_button(5), playerMove()])
    b5.place(x=117, y=155)

    b6 = Button(root, width=14, text=" ", height=7, command=lambda: [define_button(6), playerMove()])
    b6.place(x=234, y=155)

    b1 = Button(root, width=14, text=" ", height=7, command=lambda: [define_button(1), playerMove()])
    b1.place(x=0, y=280)

    b2 = Button(root, width=14, text=" ", height=7, command=lambda: [define_button(2), playerMove()])
    b2.place(x=117, y=280)

    b3 = Button(root, width=14, text=" ", height=7, command=lambda: [define_button(3), playerMove()])
    b3.place(x=234, y=280)

    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]


printboard()

global buttons


#boardcopy()
def boardcopy():
    global buttons
    root.title("TIC TAC TOE GAME")
    root.geometry("342x395+360+250")
    root.resizable(False, False)
    buttons[6].place(x=0, y=30)
    buttons[7].place(x=117, y=30)
    buttons[8].place(x=234, y=30)
    buttons[3].place(x=0, y=155)
    buttons[4].place(x=117, y=155)
    buttons[5].place(x=234, y=155)
    buttons[0].place(x=0, y=280)
    buttons[1].place(x=117, y=280)
    buttons[2].place(x=234, y=280)


title = Label(root, text = "TIC TAC TOE GAME", font = "Broadway 20")
title.place(x=35, y=-5)



chars = []


#define_button()
def define_button(number):
    return number



#insertLetter()
def insertLetter(letter, pos):
    buttons[pos - 1].config(text=letter)



#SpaceIsFree()
def SpaceIsFree(pos):
    return buttons[pos-1]['text'] == " "



#IsWinner()
def IsWinner(bu, le):
    return (bu[0]['text'] == le and bu[1]['text'] == le  and bu[2]['text'] == le ) or (bu[3]['text'] == le and bu[4]['text'] == le and bu[5]['text'] == le) or (bu[6]['text'] == le and bu[7]['text'] == le and bu[8]['text'] == le) or (bu[0]['text'] == le and bu[3]['text'] == le and bu[6]['text'] == le) or (bu[1]['text'] == le and bu[4]['text'] == le and bu[7]['text'] == le) or (bu[2]['text'] == le and bu[5]['text'] == le and bu[8]['text'] == le) or (bu[0]['text'] == le and bu[4]['text'] == le and bu[8]['text'] == le) or (bu[2]['text'] == le and bu[4]['text'] == le and bu[6]['text'] == le)



#playerMove()
def playerMove():
    run = True
    while run:
        move = simpledialog.askinteger("Input", "Enter number position according to the laptop number pad:")
        try:
            move = int(move)
            if move>0 and move<10:
                if SpaceIsFree(move):
                    run = False
                    insertLetter("X", move)
                else:
                    messagebox.showerror("Error", "This place is already occupied", icon="warning")
            else:
                messagebox.showerror("Error", "The given number is out of range", icon = "warning")
        except:
            messagebox.showerror("Error", "Please enter  a number", icon= "warning")



#compMove()
def compMove():

    move = 0

    #TO WIN OR STOP WIN

    possibleMoves = []

    for i in buttons:
        if i["text"] == " ":
            j = buttons.index(i)
            possibleMoves.append(j+1)


    for let in ["O", "X"]:
        for i in possibleMoves:
            insertLetter(let, i)

            if IsWinner(buttons, let):
                move = i
                insertLetter(" ", i)
                return move
            else:
                insertLetter(" ", i)

    #FOR CORNERS

    possibleCorners = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            possibleCorners.append(i)

    if len(possibleCorners)>0:
        move = selectRandom(possibleCorners)
        return move

    #FOR CENTER

    if 5 in possibleMoves:
        move = 5

    #FOR EDGES

    possibleEdges = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            possibleEdges.append(i)

    if len(possibleEdges) > 0:
        move = selectRandom(possibleEdges)
        return move

    return move



#selectRandom()
def selectRandom(list1):
    import random
    length = len(list1)
    r = random.randrange(0, length)
    return list1[r]



#isBoardfull()
def isBoardfull():
    # if buttons[0]["text"] == " " and buttons[1]["text"] == " " and buttons[2]["text"] == " " and buttons[3]["text"] == " " and buttons[4]["text"] == " " and buttons[5]["text"] == " " and buttons[6]["text"] == " " and buttons[7]["text"] == " " and buttons[8]["text"] == " ":
    #     return False
    # else:
    #     return True


    for i in buttons:
        a = i['text']
        chars.append(a)

    if chars.count(" ") > 1:
        return False
    else:
        return True




#mains()
def mains():
    while not(isBoardfull()):

        if not (IsWinner(buttons, "O")):
            playerMove()
        else:
            messagebox.showinfo("Info", "You have lost the game.", icon="info")
            root.destroy()


        if not (IsWinner(buttons, "X")):
            move = compMove()
            if move == 0:
                messagebox.showinfo("Info", "Tie Game", icon = "info")
                root.destroy()
            else:
                insertLetter("O", move)

        else:
            messagebox.showinfo("Info", "You have won the game.", icon="info")
            root.destroy()


    if isBoardfull():
        messagebox.showinfo("Info", "Tie Game", icon="info")

if __name__== "__main__":
    printboard()
    mains()

root.mainloop()
