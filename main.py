from tkinter import *
import os
from random import randint

cases_player = []
cases_computer = []

stop_computer_playing = 0

switchIcon = False

start_game = False
finish_game = False

Frame = Tk()

Frame.title('Tik Tac Toe - Tanguy J | Supinfo.com')
Frame.resizable(width=False, height=False)

canvas = Canvas(Frame,width=1000,height=650,bg="white")
canvas.pack()

base_folder = os.path.dirname(__file__)
image_path_bg = os.path.join(base_folder, 'imgs/background.png')
image_path_sheep = os.path.join(base_folder, 'imgs/sheep.png')
image_path_bird = os.path.join(base_folder, 'imgs/bird.png')
image_path_msg_win = os.path.join(base_folder, 'imgs/msg_win.png')
image_path_msg_lose = os.path.join(base_folder, 'imgs/msg_lose.png')
image_path_msg_draw = os.path.join(base_folder, 'imgs/msg_draw.png')
image_path_switch = os.path.join(base_folder, 'imgs/switch.png')

photo = PhotoImage(file=image_path_bg)
icon_sheep = PhotoImage(file = image_path_sheep)
icon_bird = PhotoImage(file = image_path_bird)
msg_win = PhotoImage(file = image_path_msg_win)
msg_lose = PhotoImage(file = image_path_msg_lose)
msg_draw = PhotoImage(file = image_path_msg_draw)
image_switch = PhotoImage(file = image_path_switch)

canvas.create_image(0, 0, image=photo, anchor=NW)
label_player = canvas.create_text(850,260,fill="black",font="null 20",text="Votre Pion")
label_computer = canvas.create_text(850,380,fill="black",font="null 20",text="Ordinateur")

info_txt = canvas.create_text(180,619,fill="#0A7E70",font="null 15",text="C'est à vous de jouer !")

render_switchBtn = 0

switchBtn = Button(Frame, anchor = W, image=image_switch, bg="#15BDAC", command=lambda: switchingIcon())
switchBtn.configure(width=30, height=15, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')
render_switchBtn = canvas.create_window(800, 310, anchor=NW, window=switchBtn)

case1 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(1))
case2 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(2))
case3 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(3))
case4 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(4))
case5 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(5))
case6 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(6))
case7 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(7))
case8 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(8))
case9 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(9))

case1.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')
case2.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')
case3.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')
case4.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')
case5.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')
case6.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')
case7.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')
case8.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')
case9.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')

case1_render = 0
case2_render = 0
case3_render = 0
case4_render = 0
case5_render = 0
case6_render = 0
case7_render = 0
case8_render = 0
case9_render = 0

def createCasesButton():
    global case1_render
    global case2_render
    global case3_render
    global case4_render
    global case5_render
    global case6_render
    global case7_render
    global case8_render
    global case9_render

    case1_render = canvas.create_window(39, 60, anchor=NW, window=case1)
    case2_render = canvas.create_window(213, 60, anchor=NW, window=case2)
    case3_render = canvas.create_window(389, 60, anchor=NW, window=case3)
    case4_render = canvas.create_window(39, 237, anchor=NW, window=case4)
    case5_render = canvas.create_window(213, 235, anchor=NW, window=case5)
    case6_render = canvas.create_window(389, 235, anchor=NW, window=case6)
    case7_render = canvas.create_window(39, 413, anchor=NW, window=case7)
    case8_render = canvas.create_window(213, 413, anchor=NW, window=case8)
    case9_render = canvas.create_window(389, 413, anchor=NW, window=case9)

createCasesButton()


def switchingIcon():
    global switchIcon

    if switchIcon == False and start_game == False:
        canvas.itemconfigure(label_player, text="Ordinateur")
        canvas.itemconfigure(label_computer, text="Votre Pion")
        switchIcon = True
    elif switchIcon == True and start_game == False:
        canvas.itemconfigure(label_player, text="Votre Pion")
        canvas.itemconfigure(label_computer, text="Ordinateur")
        switchIcon = False


player_play = 1

def setCaseIcon(caseId):
    global player_play
    global cases_player
    global start_game

    if start_game == False:
        start_game = True

    if player_play == 1:
        deleteCase(caseId)
        if switchIcon == False:
            setIcon(1, caseId)
        else:
            setIcon(0, caseId)
        player_play = 0
        cases_player.insert(0, caseId)
        verifyWin()
        if stop_computer_playing == 0:
            playComputer()
        # canvas.itemconfigure(info_txt, text="C'est à l'Ordinateur de jouer ...")
        # canvas.coords(info_txt, 215, 619)

def deleteCase(caseId):
    if caseId == 1:
        canvas.delete(case1_render)
    if caseId == 2:
        canvas.delete(case2_render)
    if caseId == 3:
        canvas.delete(case3_render)
    if caseId == 4:
        canvas.delete(case4_render)
    if caseId == 5:
        canvas.delete(case5_render)
    if caseId == 6:
        canvas.delete(case6_render)
    if caseId == 7:
        canvas.delete(case7_render)
    if caseId == 8:
        canvas.delete(case8_render)
    if caseId == 9:
        canvas.delete(case9_render)


icon_bird1_render = 0
icon_bird2_render = 0
icon_bird3_render = 0
icon_bird4_render = 0
icon_bird5_render = 0
icon_bird6_render = 0
icon_bird7_render = 0
icon_bird8_render = 0
icon_bird9_render = 0

icon_sheep1_render = 0
icon_sheep2_render = 0
icon_sheep3_render = 0
icon_sheep4_render = 0
icon_sheep5_render = 0
icon_sheep6_render = 0
icon_sheep7_render = 0
icon_sheep8_render = 0
icon_sheep9_render = 0

def setIcon(iconType, caseId):
    global icon_bird1_render
    global icon_bird2_render
    global icon_bird3_render
    global icon_bird4_render
    global icon_bird5_render
    global icon_bird6_render
    global icon_bird7_render
    global icon_bird8_render
    global icon_bird9_render

    global icon_sheep1_render
    global icon_sheep2_render
    global icon_sheep3_render
    global icon_sheep4_render
    global icon_sheep5_render
    global icon_sheep6_render
    global icon_sheep7_render
    global icon_sheep8_render
    global icon_sheep9_render

    if iconType == 0:
        if caseId == 1:
            icon_bird1_render = canvas.create_image(60,80,image=icon_bird,anchor=NW)
        if caseId == 2:
            icon_bird2_render = canvas.create_image(240,80,image=icon_bird,anchor=NW) 
        if caseId == 3:
            icon_bird3_render = canvas.create_image(420,80,image=icon_bird,anchor=NW) 
        if caseId == 4:
            icon_bird4_render = canvas.create_image(60,260,image=icon_bird,anchor=NW)
        if caseId == 5:
            icon_bird5_render = canvas.create_image(240,260,image=icon_bird,anchor=NW) 
        if caseId == 6:
            icon_bird6_render = canvas.create_image(420,260,image=icon_bird,anchor=NW)
        if caseId == 7:
            icon_bird7_render = canvas.create_image(60,440,image=icon_bird,anchor=NW)
        if caseId == 8:
            icon_bird8_render = canvas.create_image(240,440,image=icon_bird,anchor=NW) 
        if caseId == 9:
            icon_bird9_render = canvas.create_image(420,440,image=icon_bird,anchor=NW) 

    else:
        if caseId == 1:
            icon_sheep1_render = canvas.create_image(60,80,image=icon_sheep,anchor=NW)
        if caseId == 2:
            icon_sheep2_render = canvas.create_image(240,80,image=icon_sheep,anchor=NW) 
        if caseId == 3:
            icon_sheep3_render = canvas.create_image(420,80,image=icon_sheep,anchor=NW) 
        if caseId == 4:
            icon_sheep4_render = canvas.create_image(60,260,image=icon_sheep,anchor=NW)
        if caseId == 5:
            icon_sheep5_render = canvas.create_image(240,260,image=icon_sheep,anchor=NW) 
        if caseId == 6:
            icon_sheep6_render = canvas.create_image(420,260,image=icon_sheep,anchor=NW)
        if caseId == 7:
            icon_sheep7_render = canvas.create_image(60,440,image=icon_sheep,anchor=NW)
        if caseId == 8:
            icon_sheep8_render = canvas.create_image(240,440,image=icon_sheep,anchor=NW) 
        if caseId == 9:
            icon_sheep9_render = canvas.create_image(420,440,image=icon_sheep,anchor=NW)       

def deleteIcons():
    global icon_bird1_render
    global icon_bird2_render
    global icon_bird3_render
    global icon_bird4_render
    global icon_bird5_render
    global icon_bird6_render
    global icon_bird7_render
    global icon_bird8_render
    global icon_bird9_render

    global icon_sheep1_render
    global icon_sheep2_render
    global icon_sheep3_render
    global icon_sheep4_render
    global icon_sheep5_render
    global icon_sheep6_render
    global icon_sheep7_render
    global icon_sheep8_render
    global icon_sheep9_render

    canvas.delete(icon_bird1_render)
    canvas.delete(icon_bird2_render)
    canvas.delete(icon_bird3_render)
    canvas.delete(icon_bird4_render)
    canvas.delete(icon_bird5_render)
    canvas.delete(icon_bird6_render)
    canvas.delete(icon_bird7_render)
    canvas.delete(icon_bird8_render)
    canvas.delete(icon_bird9_render)

    canvas.delete(icon_sheep1_render)
    canvas.delete(icon_sheep2_render)
    canvas.delete(icon_sheep3_render)
    canvas.delete(icon_sheep4_render)
    canvas.delete(icon_sheep5_render)
    canvas.delete(icon_sheep6_render)
    canvas.delete(icon_sheep7_render)
    canvas.delete(icon_sheep8_render)
    canvas.delete(icon_sheep9_render)

    # for i in range(i, i+len(cases_player)+len(cases_computer)+1):
    #     canvas.delete(i)


def playComputer():
    global player_play
    global cases_computer

    random_case = randint(1,9)

    if(random_case in cases_computer):
        playComputer()
    elif(random_case in cases_player):
        playComputer()
    else:
        deleteCase(random_case)
        if switchIcon == False:
            setIcon(0, random_case)
        else:
            setIcon(1, random_case)
        player_play = 1
        cases_computer.insert(0, random_case)
        verifyWin()
        canvas.itemconfigure(info_txt, text="C'est à vous de jouer !")
        canvas.coords(info_txt, 180, 619)

# 0 = no win | 1 = player win | 2 = computer win
entity_win = 0

def verifyWin() :
    global entity_win
    global stop_computer_playing

    if(1 in cases_player and 2 in cases_player and 3 in cases_player):
        entity_win = 1
    if(4 in cases_player and 5 in cases_player and 6 in cases_player):
        entity_win = 1
    if(7 in cases_player and 8 in cases_player and 9 in cases_player):
        entity_win = 1
    if(1 in cases_player and 4 in cases_player and 7 in cases_player):
        entity_win = 1
    if(2 in cases_player and 5 in cases_player and 8 in cases_player):
        entity_win = 1
    if(3 in cases_player and 6 in cases_player and 9 in cases_player):
        entity_win = 1
    if(1 in cases_player and 5 in cases_player and 9 in cases_player):
        entity_win = 1
    if(3 in cases_player and 5 in cases_player and 7 in cases_player):
        entity_win = 1

    if(1 in cases_computer and 2 in cases_computer and 3 in cases_computer):
        entity_win = 2
    if(4 in cases_computer and 5 in cases_computer and 6 in cases_computer):
        entity_win = 2
    if(7 in cases_computer and 8 in cases_computer and 9 in cases_computer):
        entity_win = 2
    if(1 in cases_computer and 4 in cases_computer and 7 in cases_computer):
        entity_win = 2
    if(2 in cases_computer and 5 in cases_computer and 8 in cases_computer):
        entity_win = 2
    if(3 in cases_computer and 6 in cases_computer and 9 in cases_computer):
        entity_win = 2
    if(1 in cases_computer and 5 in cases_computer and 9 in cases_computer):
        entity_win = 2
    if(3 in cases_computer and 5 in cases_computer and 7 in cases_computer):
        entity_win = 2

    if entity_win == 1:
        print("Joueur gagne !")
        stop_computer_playing = 1
        printGameMsg(1)
    if entity_win == 2:  
        print("Ordinateur gagne !")  
        stop_computer_playing = 1
        printGameMsg(2)

    cases_total = len(cases_player) + len(cases_computer)
    if(cases_total == 9 and entity_win == 0):
        print("Match nul !")
        stop_computer_playing = 1
        printGameMsg(0)


image_msg_delete = 0

# 0 = match nul | 1 = joueur gagne | 2 = ordinateur gagne
def printGameMsg(gameStat):
    global finish_game
    global image_msg_delete
    global render_switchBtn

    for i in range(9):
        deleteCase(i+1)

    canvas.delete(render_switchBtn)

    if gameStat == 0:
        image_draw = canvas.create_image(180, 130, image=msg_draw, anchor=NW)
        image_msg_delete = image_draw
    elif gameStat == 1:
        image_win = canvas.create_image(180, 130, image=msg_win, anchor=NW)
        image_msg_delete = image_win
    elif gameStat == 2:
        image_lose = canvas.create_image(180, 130, image=msg_lose, anchor=NW)
        image_msg_delete = image_lose

    finish_game = True


def reloadGame():
    global image_msg_delete
    global start_game
    global player_play
    global entity_win
    global image_msg_delete
    global stop_computer_playing
    global render_switchBtn

    canvas.delete(image_msg_delete)
    deleteIcons()
    createCasesButton()

    start_game = False
    render_switchBtn = canvas.create_window(800, 310, anchor=NW, window=switchBtn)

    del cases_player[:]
    del cases_computer[:]

    player_play = 1
    entity_win = 0
    image_msg_delete = 0
    stop_computer_playing = 0


def mouseClickLeftButton(event):
    global finish_game

    if finish_game == True:
        reloadGame()
        finish_game = False


Frame.bind("<Button-1>", mouseClickLeftButton)

Frame.mainloop()
