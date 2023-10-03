from tkinter import *
import random


root = Tk()
root.title('Mastermind')
root.iconbitmap('png\\lamp.ico')
root.geometry("610x650")
root.resizable(0,0)


raw_choice = [0, 0, 0, 0, 0, 0]
user_choice = []
choice_limits = 0
start = 0


def click_blue():
    global raw_choice
    if raw_choice[0] > 0:
        raw_choice[0] = 0
    else:
        raw_choice[0] = 1
    global choice_limits
    choice_limits += 1
    label_view()
        
def click_green():
    global raw_choice
    if raw_choice[1] > 0:
        raw_choice[1] = 0
    else:
        raw_choice[1] = 1
    global choice_limits
    choice_limits += 1
    label_view()

def click_light_blue():
    global raw_choice
    if raw_choice[2] > 0:
        raw_choice[2] = 0
    else:
        raw_choice[2] = 1
    global choice_limits
    choice_limits += 1
    label_view()

def click_orange():
    global raw_choice
    if raw_choice[3] > 0:
        raw_choice[3] = 0
    else:
        raw_choice[3] = 1
    global choice_limits
    choice_limits += 1
    label_view()

def click_red():
    global raw_choice
    if raw_choice[4] > 0:
        raw_choice[4] = 0
    else:
        raw_choice[4] = 1
    global choice_limits
    choice_limits += 1
    label_view()

def click_yellow():
    global raw_choice
    if raw_choice[5] > 0:
        raw_choice[5] = 0
    else:
        raw_choice[5] = 1
    global choice_limits
    choice_limits += 1
    label_view()

def computer_choice():
    global color_choice
    label_view_list = [label_view1, label_view2, label_view3, label_view4, label_view5, label_view6]
    if start == 1:
        color_choice = random.sample(range(6), k=4)

    result_view()

def click_start():
    global start
    if choice_limits == 4:
        start = 1
        computer_choice()
    elif choice_limits == 8:
        start = 2
        computer_choice()
    elif choice_limits == 12:
        start = 3
        computer_choice()
    elif choice_limits == 16:
        start = 4
        computer_choice()
    elif choice_limits == 20:
        start = 5
        computer_choice()
    elif choice_limits == 24:
        start = 6
        computer_choice()

def click_delete():
    global choice_limits
    global user_choice
    
    if start == 0:
        if choice_limits == 1:
            label_empty().place(x=20, y=150)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 2:
            label_empty().place(x=60, y=150)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 3:
            label_empty().place(x=100, y=150)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 4:
            label_empty().place(x=140, y=150)
            choice_limits -= 1
            user_choice.pop()

    if start == 1:
        if choice_limits == 5:
            label_empty().place(x=20, y=210)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 6:
            label_empty().place(x=60, y=210)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 7:
            label_empty().place(x=100, y=210)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 8:
            label_empty().place(x=140, y=210)
            choice_limits -= 1
            user_choice.pop()

    if start == 2:
        if choice_limits == 9:
            label_empty().place(x=20, y=270)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 10:
            label_empty().place(x=60, y=270)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 11:
            label_empty().place(x=100, y=270)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 12:
            label_empty().place(x=140, y=270)
            choice_limits -= 1
            user_choice.pop()

    if start == 3:
        if choice_limits == 13:
            label_empty().place(x=20, y=330)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 14:
            label_empty().place(x=60, y=330)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 15:
            label_empty().place(x=100, y=330)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 16:
            label_empty().place(x=140, y=330)
            choice_limits -= 1
            user_choice.pop()

    if start == 4:
        if choice_limits == 17:
            label_empty().place(x=20, y=390)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 18:
            label_empty().place(x=60, y=390)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 19:
            label_empty().place(x=100, y=390)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 20:
            label_empty().place(x=140, y=390)
            choice_limits -= 1
            user_choice.pop()

    if start == 5:
        if choice_limits == 21:
            label_empty().place(x=20, y=450)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 22:
            label_empty().place(x=60, y=450)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 23:
            label_empty().place(x=100, y=450)
            choice_limits -= 1
            user_choice.pop()
        if choice_limits == 24:
            label_empty().place(x=140, y=450)
            choice_limits -= 1
            user_choice.pop()

def click_restart():
    global raw_choice
    global user_choice
    global choice_limits
    global start
    raw_choice = [0, 0, 0, 0, 0, 0]
    user_choice.clear()
    choice_limits = 0
    start = 0
    label_restart().place(x=10, y=10)

def result_view():
    global choice_limits
    global start
    global user_choice
    global label_view_list
    label_view_list = [label_view1, label_view2, label_view3, label_view4, label_view5, label_view6]
    match = []
    member = []

    for i, (user, computer) in enumerate(zip(user_choice, color_choice)):
        if user == computer:
            match.append(user)
        if user in color_choice and user != computer:
            member.append(user)

    if member:
        if match:
            for x in set(member):
                if x in set(match):
                    member.remove(x)
    if member:
        if match:
            for x in set(member):
                if x in set(match):
                    member.remove(x)
    if member:
        if match:
            for x in set(member):
                if x in set(match):
                    member.remove(x)

    member = set(member)
    member = list(member)
    user_choice.clear()

    if start == 1:
        if len(match) == 4:
            label_result1().place(x=250, y=150)
            label_result1().place(x=300, y=150)
            label_result1().place(x=350, y=150)
            label_result1().place(x=400, y=150)

            for i, view in enumerate(color_choice):
                if i == 0:
                    label_view_list[view]().place(x=150, y=50)
                if i == 1:
                    label_view_list[view]().place(x=190, y=50)
                if i == 2:
                    label_view_list[view]().place(x=230, y=50)
                if i == 3:
                    label_view_list[view]().place(x=270, y=50)

            label_win().place(x=10, y=10)

        if len(match) == 3:
            label_result1().place(x=250, y=150)
            label_result1().place(x=300, y=150)
            label_result1().place(x=350, y=150)

        if len(match) == 2 and len(member) == 0:
            label_result1().place(x=250, y=150)
            label_result1().place(x=300, y=150)

        if len(member) == 4:
            label_result2().place(x=250, y=150)
            label_result2().place(x=300, y=150)
            label_result2().place(x=350, y=150)
            label_result2().place(x=400, y=150)

        if len(member) == 3 and len(match) == 0:
            label_result2().place(x=250, y=150)
            label_result2().place(x=300, y=150)
            label_result2().place(x=350, y=150)

        if len(member) == 2 and len(match) == 0:
            label_result2().place(x=250, y=150)
            label_result2().place(x=300, y=150)

        if len(member) == 1 and len(match) == 0:
            label_result2().place(x=250, y=150)

        if len(match) == 2 and len(member) == 2:
            label_result1().place(x=250, y=150)
            label_result1().place(x=300, y=150)
            label_result2().place(x=350, y=150)
            label_result2().place(x=400, y=150)

        if len(match) == 1 and len(member) == 1:
            label_result1().place(x=250, y=150)
            label_result2().place(x=300, y=150)

        if len(match) == 1 and len(member) == 0:
            label_result1().place(x=250, y=150)

        if len(member) == 3 and len(match) == 1:
            label_result1().place(x=250, y=150)
            label_result2().place(x=300, y=150)
            label_result2().place(x=350, y=150)
            label_result2().place(x=400, y=150)

        if len(match) == 2 and len(member) == 1:
            label_result1().place(x=250, y=150)
            label_result1().place(x=300, y=150)
            label_result2().place(x=350, y=150)

        if len(member) == 2 and len(match) == 1:
            label_result1().place(x=250, y=150)
            label_result2().place(x=300, y=150)
            label_result2().place(x=350, y=150)

        match.clear()
        member.clear()

    if start == 2:
        if len(match) == 4:
            label_result1().place(x=250, y=210)
            label_result1().place(x=300, y=210)
            label_result1().place(x=350, y=210)
            label_result1().place(x=400, y=210)

            for i, view in enumerate(color_choice):
                if i == 0:
                    label_view_list[view]().place(x=150, y=50)
                if i == 1:
                    label_view_list[view]().place(x=190, y=50)
                if i == 2:
                    label_view_list[view]().place(x=230, y=50)
                if i == 3:
                    label_view_list[view]().place(x=270, y=50)

            label_win().place(x=10, y=10)

        if len(match) == 3:
            label_result1().place(x=250, y=210)
            label_result1().place(x=300, y=210)
            label_result1().place(x=350, y=210)

        if len(match) == 2 and len(member) == 0:
            label_result1().place(x=250, y=210)
            label_result1().place(x=300, y=210)

        if len(member) == 4:
            label_result2().place(x=250, y=210)
            label_result2().place(x=300, y=210)
            label_result2().place(x=350, y=210)
            label_result2().place(x=400, y=210)

        if len(member) == 3 and len(match) == 0:
            label_result2().place(x=250, y=210)
            label_result2().place(x=300, y=210)
            label_result2().place(x=350, y=210)

        if len(member) == 2 and len(match) == 0:
            label_result2().place(x=250, y=210)
            label_result2().place(x=300, y=210)

        if len(member) == 1 and len(match) == 0:
            label_result2().place(x=250, y=210)

        if len(match) == 2 and len(member) == 2:
            label_result1().place(x=250, y=210)
            label_result1().place(x=300, y=210)
            label_result2().place(x=350, y=210)
            label_result2().place(x=400, y=210)

        if len(match) == 1 and len(member) == 1:
            label_result1().place(x=250, y=210)
            label_result2().place(x=300, y=210)

        if len(match) == 1 and len(member) == 0:
            label_result1().place(x=250, y=210)

        if len(member) == 3 and len(match) == 1:
            label_result1().place(x=250, y=210)
            label_result2().place(x=300, y=210)
            label_result2().place(x=350, y=210)
            label_result2().place(x=400, y=210)

        if len(match) == 2 and len(member) == 1:
            label_result1().place(x=250, y=210)
            label_result1().place(x=300, y=210)
            label_result2().place(x=350, y=210)

        if len(member) == 2 and len(match) == 1:
            label_result1().place(x=250, y=210)
            label_result2().place(x=300, y=210)
            label_result2().place(x=350, y=210)

        match.clear()
        member.clear()

    if start == 3:
        if len(match) == 4:
            label_result1().place(x=250, y=270)
            label_result1().place(x=300, y=270)
            label_result1().place(x=350, y=270)
            label_result1().place(x=400, y=270)

            for i, view in enumerate(color_choice):
                if i == 0:
                    label_view_list[view]().place(x=150, y=50)
                if i == 1:
                    label_view_list[view]().place(x=190, y=50)
                if i == 2:
                    label_view_list[view]().place(x=230, y=50)
                if i == 3:
                    label_view_list[view]().place(x=270, y=50)

            label_win().place(x=10, y=10)

        if len(match) == 3:
            label_result1().place(x=250, y=270)
            label_result1().place(x=300, y=270)
            label_result1().place(x=350, y=270)

        if len(match) == 2 and len(member) == 0:
            label_result1().place(x=250, y=270)
            label_result1().place(x=300, y=270)

        if len(member) == 4:
            label_result2().place(x=250, y=270)
            label_result2().place(x=300, y=270)
            label_result2().place(x=350, y=270)
            label_result2().place(x=400, y=270)

        if len(member) == 3 and len(match) == 0:
            label_result2().place(x=250, y=270)
            label_result2().place(x=300, y=270)
            label_result2().place(x=350, y=270)

        if len(member) == 2 and len(match) == 0:
            label_result2().place(x=250, y=270)
            label_result2().place(x=300, y=270)

        if len(member) == 1 and len(match) == 0:
            label_result2().place(x=250, y=270)

        if len(match) == 2 and len(member) == 2:
            label_result1().place(x=250, y=270)
            label_result1().place(x=300, y=270)
            label_result2().place(x=350, y=270)
            label_result2().place(x=400, y=270)

        if len(match) == 1 and len(member) == 1:
            label_result1().place(x=250, y=270)
            label_result2().place(x=300, y=270)

        if len(match) == 1 and len(member) == 0:
            label_result1().place(x=250, y=270)

        if len(member) == 3 and len(match) == 1:
            label_result1().place(x=250, y=270)
            label_result2().place(x=300, y=270)
            label_result2().place(x=350, y=270)
            label_result2().place(x=400, y=270)

        if len(match) == 2 and len(member) == 1:
            label_result1().place(x=250, y=270)
            label_result1().place(x=300, y=270)
            label_result2().place(x=350, y=270)

        if len(member) == 2 and len(match) == 1:
            label_result1().place(x=250, y=270)
            label_result2().place(x=300, y=270)
            label_result2().place(x=350, y=270)

        match.clear()
        member.clear()

    if start == 4:
        if len(match) == 4:
            label_result1().place(x=250, y=330)
            label_result1().place(x=300, y=330)
            label_result1().place(x=350, y=330)
            label_result1().place(x=400, y=330)

            for i, view in enumerate(color_choice):
                if i == 0:
                    label_view_list[view]().place(x=150, y=50)
                if i == 1:
                    label_view_list[view]().place(x=190, y=50)
                if i == 2:
                    label_view_list[view]().place(x=230, y=50)
                if i == 3:
                    label_view_list[view]().place(x=270, y=50)

            label_win().place(x=10, y=10)

        if len(match) == 3:
            label_result1().place(x=250, y=330)
            label_result1().place(x=300, y=330)
            label_result1().place(x=350, y=330)

        if len(match) == 2 and len(member) == 0:
            label_result1().place(x=250, y=330)
            label_result1().place(x=300, y=330)

        if len(member) == 4:
            label_result2().place(x=250, y=330)
            label_result2().place(x=300, y=330)
            label_result2().place(x=350, y=330)
            label_result2().place(x=400, y=330)

        if len(member) == 3 and len(match) == 0:
            label_result2().place(x=250, y=330)
            label_result2().place(x=300, y=330)
            label_result2().place(x=350, y=330)

        if len(member) == 2 and len(match) == 0:
            label_result2().place(x=250, y=330)
            label_result2().place(x=300, y=330)

        if len(member) == 1 and len(match) == 0:
            label_result2().place(x=250, y=330)

        if len(match) == 2 and len(member) == 2:
            label_result1().place(x=250, y=330)
            label_result1().place(x=300, y=330)
            label_result2().place(x=350, y=330)
            label_result2().place(x=400, y=330)

        if len(match) == 1 and len(member) == 1:
            label_result1().place(x=250, y=330)
            label_result2().place(x=300, y=330)

        if len(match) == 1 and len(member) == 0:
            label_result1().place(x=250, y=330)

        if len(member) == 3 and len(match) == 1:
            label_result1().place(x=250, y=330)
            label_result2().place(x=300, y=330)
            label_result2().place(x=350, y=330)
            label_result2().place(x=400, y=330)

        if len(match) == 2 and len(member) == 1:
            label_result1().place(x=250, y=330)
            label_result1().place(x=300, y=330)
            label_result2().place(x=350, y=330)

        if len(member) == 2 and len(match) == 1:
            label_result1().place(x=250, y=330)
            label_result2().place(x=300, y=330)
            label_result2().place(x=350, y=330)

        match.clear()
        member.clear()

    if start == 5:
        if len(match) == 4:
            label_result1().place(x=250, y=390)
            label_result1().place(x=300, y=390)
            label_result1().place(x=350, y=390)
            label_result1().place(x=400, y=390)

            for i, view in enumerate(color_choice):
                if i == 0:
                    label_view_list[view]().place(x=150, y=50)
                if i == 1:
                    label_view_list[view]().place(x=190, y=50)
                if i == 2:
                    label_view_list[view]().place(x=230, y=50)
                if i == 3:
                    label_view_list[view]().place(x=270, y=50)

            label_win().place(x=10, y=10)

        if len(match) == 3:
            label_result1().place(x=250, y=390)
            label_result1().place(x=300, y=390)
            label_result1().place(x=350, y=390)

        if len(match) == 2 and len(member) == 0:
            label_result1().place(x=250, y=390)
            label_result1().place(x=300, y=390)

        if len(member) == 4:
            label_result2().place(x=250, y=390)
            label_result2().place(x=300, y=390)
            label_result2().place(x=350, y=390)
            label_result2().place(x=400, y=390)

        if len(member) == 3 and len(match) == 0:
            label_result2().place(x=250, y=390)
            label_result2().place(x=300, y=390)
            label_result2().place(x=350, y=390)

        if len(member) == 2 and len(match) == 0:
            label_result2().place(x=250, y=390)
            label_result2().place(x=300, y=390)

        if len(member) == 1 and len(match) == 0:
            label_result2().place(x=250, y=390)

        if len(match) == 2 and len(member) == 2:
            label_result1().place(x=250, y=390)
            label_result1().place(x=300, y=390)
            label_result2().place(x=350, y=390)
            label_result2().place(x=400, y=390)

        if len(match) == 1 and len(member) == 1:
            label_result1().place(x=250, y=390)
            label_result2().place(x=300, y=390)

        if len(match) == 1 and len(member) == 0:
            label_result1().place(x=250, y=390)

        if len(member) == 3 and len(match) == 1:
            label_result1().place(x=250, y=390)
            label_result2().place(x=300, y=390)
            label_result2().place(x=350, y=390)
            label_result2().place(x=400, y=390)

        if len(match) == 2 and len(member) == 1:
            label_result1().place(x=250, y=390)
            label_result1().place(x=300, y=390)
            label_result2().place(x=350, y=390)

        if len(member) == 2 and len(match) == 1:
            label_result1().place(x=250, y=390)
            label_result2().place(x=300, y=390)
            label_result2().place(x=350, y=390)

        match.clear()
        member.clear()

    if start == 6:
        if len(match) == 4:
            label_result1().place(x=250, y=450)
            label_result1().place(x=300, y=450)
            label_result1().place(x=350, y=450)
            label_result1().place(x=400, y=450)

            for i, view in enumerate(color_choice):
                if i == 0:
                    label_view_list[view]().place(x=150, y=50)
                if i == 1:
                    label_view_list[view]().place(x=190, y=50)
                if i == 2:
                    label_view_list[view]().place(x=230, y=50)
                if i == 3:
                    label_view_list[view]().place(x=270, y=50)

            label_win().place(x=10, y=10)

        if len(match) == 3:
            label_result1().place(x=250, y=450)
            label_result1().place(x=300, y=450)
            label_result1().place(x=350, y=450)

        if len(match) == 2 and len(member) == 0:
            label_result1().place(x=250, y=450)
            label_result1().place(x=300, y=450)

        if len(member) == 4:
            label_result2().place(x=250, y=450)
            label_result2().place(x=300, y=450)
            label_result2().place(x=350, y=450)
            label_result2().place(x=400, y=450)

        if len(member) == 3 and len(match) == 0:
            label_result2().place(x=250, y=450)
            label_result2().place(x=300, y=450)
            label_result2().place(x=350, y=450)

        if len(member) == 2 and len(match) == 0:
            label_result2().place(x=250, y=450)
            label_result2().place(x=300, y=450)

        if len(member) == 1 and len(match) == 0:
            label_result2().place(x=250, y=450)

        if len(match) == 2 and len(member) == 2:
            label_result1().place(x=250, y=450)
            label_result1().place(x=300, y=450)
            label_result2().place(x=350, y=450)
            label_result2().place(x=400, y=450)

        if len(match) == 1 and len(member) == 1:
            label_result1().place(x=250, y=450)
            label_result2().place(x=300, y=450)

        if len(match) == 1 and len(member) == 0:
            label_result1().place(x=250, y=450)

        if len(member) == 3 and len(match) == 1:
            label_result1().place(x=250, y=450)
            label_result2().place(x=300, y=450)
            label_result2().place(x=350, y=450)
            label_result2().place(x=400, y=450)

        if len(match) == 2 and len(member) == 1:
            label_result1().place(x=250, y=450)
            label_result1().place(x=300, y=450)
            label_result2().place(x=350, y=450)

        if len(member) == 2 and len(match) == 1:
            label_result1().place(x=250, y=450)
            label_result2().place(x=300, y=450)
            label_result2().place(x=350, y=450)

        if len(match) != 4:

            for i, view in enumerate(color_choice):
                if i == 0:
                    label_view_list[view]().place(x=150, y=50)
                if i == 1:
                    label_view_list[view]().place(x=190, y=50)
                if i == 2:
                    label_view_list[view]().place(x=230, y=50)
                if i == 3:
                    label_view_list[view]().place(x=270, y=50)

            label_lose().place(x=10, y=10)

        match.clear()
        member.clear()

def label_view():

    label_view_list = [label_view1, label_view2, label_view3, label_view4, label_view5, label_view6]
    global user_choice
    global raw_choice
    global choice_limits
    global start
    if choice_limits == 1:
        for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
            if number == 1:
                label().place(x=20, y=150)
                user_choice.append(i)
                raw_choice[i] = 0
    if choice_limits == 2:
        for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
            if number == 1:
                label().place(x=60, y=150)
                user_choice.append(i)
                raw_choice[i] = 0
    if choice_limits == 3:
        for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
            if number == 1:
                label().place(x=100, y=150)
                user_choice.append(i)
                raw_choice[i] = 0
    if choice_limits == 4:
        for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
            if number == 1:
                label().place(x=140, y=150)
                user_choice.append(i)
                raw_choice[i] = 0

    if choice_limits > 4 and start == 0:
        choice_limits = 4

    if start == 1:
        if choice_limits == 5:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=20, y=210)
                    user_choice.append(i)
                    raw_choice[i] = 0
        if choice_limits == 6:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=60, y=210)
                    user_choice.append(i)
                    raw_choice[i] = 0
        if choice_limits == 7:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=100, y=210)
                    user_choice.append(i)
                    raw_choice[i] = 0
        if choice_limits == 8:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=140, y=210)
                    user_choice.append(i)
                    raw_choice[i] = 0

    if choice_limits > 8 and start == 1:
        choice_limits = 8

    if start == 2:
        if choice_limits == 9:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=20, y=270)
                    user_choice.append(i)
                    raw_choice[i] = 0
        if choice_limits == 10:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=60, y=270)
                    user_choice.append(i)
                    raw_choice[i] = 0
        if choice_limits == 11:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=100, y=270)
                    user_choice.append(i)
                    raw_choice[i] = 0
        if choice_limits == 12:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=140, y=270)
                    user_choice.append(i)
                    raw_choice[i] = 0

    if choice_limits > 12 and start == 2:
        choice_limits = 12

    if start == 3:
        if choice_limits == 13:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=20, y=330)
                    user_choice.append(i)
                    raw_choice[i] = 0
        if choice_limits == 14:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=60, y=330)
                    user_choice.append(i)
                    raw_choice[i] = 0
        if choice_limits == 15:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=100, y=330)
                    user_choice.append(i)
                    raw_choice[i] = 0
        if choice_limits == 16:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=140, y=330)
                    user_choice.append(i)
                    raw_choice[i] = 0

    if choice_limits > 16 and start == 3:
        choice_limits = 16

    if start == 4:
        if choice_limits == 17:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=20, y=390)
                    user_choice.append(i)
                    raw_choice[i] = 0
        if choice_limits == 18:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=60, y=390)
                    user_choice.append(i)
                    raw_choice[i] = 0
        if choice_limits == 19:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=100, y=390)
                    user_choice.append(i)
                    raw_choice[i] = 0
        if choice_limits == 20:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=140, y=390)
                    user_choice.append(i)
                    raw_choice[i] = 0

    if choice_limits > 20 and start == 4:
        choice_limits = 20

    if start == 5:
        if choice_limits == 21:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=20, y=450)
                    user_choice.append(i)
                    raw_choice[i] = 0
        if choice_limits == 22:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=60, y=450)
                    user_choice.append(i)
                    raw_choice[i] = 0
        if choice_limits == 23:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=100, y=450)
                    user_choice.append(i)
                    raw_choice[i] = 0
        if choice_limits == 24:
            for i, (number, label) in enumerate(zip(raw_choice, label_view_list)):
                if number == 1:
                    label().place(x=140, y=450)
                    user_choice.append(i)
                    raw_choice[i] = 0


color_choice1 = PhotoImage(file='png\\blue-chrome-button.png')
color_choice2 = PhotoImage(file='png\\green-chrome-button.png')
color_choice3 = PhotoImage(file='png\\light-blue-chrome-button.png')
color_choice4 = PhotoImage(file='png\\orange-chrome.png')
color_choice5 = PhotoImage(file='png\\red-chrome.png')
color_choice6 = PhotoImage(file='png\\yellow-chrome-button.png')

ok_choice = PhotoImage(file='png\\ok.png')
cancel_choice = PhotoImage(file='png\\backspace.png')
restart_choice = PhotoImage(file='png\\restart.png')

color_view1 = PhotoImage(file='png\\blue.png')
color_view2 = PhotoImage(file='png\\green.png')
color_view3 = PhotoImage(file='png\\light-blue.png')
color_view4 = PhotoImage(file='png\\orange.png')
color_view5 = PhotoImage(file='png\\red.png')
color_view6 = PhotoImage(file='png\\yellow.png')

result_view1 = PhotoImage(file='png\\ex.png')
result_view2 = PhotoImage(file='png\\plus.png')

win_view = PhotoImage(file='png\\trophy.png')
lose_view = PhotoImage(file='png\\game_over.png')

empty_view = PhotoImage(file='png\\empty1.png')
restart_view = PhotoImage(file='png\\play_again.png')

label_view1 = lambda:Label(image=color_view1)
label_view2 = lambda:Label(image=color_view2)
label_view3 = lambda:Label(image=color_view3)
label_view4 = lambda:Label(image=color_view4)
label_view5 = lambda:Label(image=color_view5)
label_view6 = lambda:Label(image=color_view6)

label_result1 = lambda:Label(image=result_view1)
label_result2 = lambda:Label(image=result_view2)

label_win = lambda:Label(image=win_view)
label_lose = lambda:Label(image=lose_view)

label_empty = lambda:Label(image=empty_view)
label_restart = lambda:Label(image=restart_view)

choice_button1 = Button(root, image=color_choice1, command=click_blue, borderwidth=0)
choice_button1.place(x=10, y=550)
choice_button2 = Button(root, image=color_choice2, command=click_green, borderwidth=0)
choice_button2.place(x=110, y=550)
choice_button3 = Button(root, image=color_choice3, command=click_light_blue, borderwidth=0)
choice_button3.place(x=210, y=550)
choice_button4 = Button(root, image=color_choice4, command=click_orange, borderwidth=0)
choice_button4.place(x=310, y=550)
choice_button5 = Button(root, image=color_choice5, command=click_red, borderwidth=0)
choice_button5.place(x=410, y=550)
choice_button6 = Button(root, image=color_choice6, command=click_yellow, borderwidth=0)
choice_button6.place(x=510, y=550)

start_button = Button(root, image=ok_choice, command=click_start, borderwidth=0)
start_button.place(x=470, y=320)
delete_button = Button(root, image=cancel_choice, command=click_delete, borderwidth=0)
delete_button.place(x=470, y=170)
restart_button = Button(root, image=restart_choice, command=click_restart, borderwidth=0)
restart_button.place(x=470, y=30)


root.mainloop()
