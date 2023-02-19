#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------- NEO VIRTUAL ASSISTANT PROJECT by: STEPHEN MATTHEW SIRAMBANG  --------------------------------------------------------# 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

import customtkinter
import threading
import keyboard
import time
import speech_recognition
import subprocess
import pyautogui as pg
import os
import sys
import requests
import json
import requests
import base64
import pygame

from os import environ
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
from tkinter import messagebox
from cryptography.fernet import Fernet

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # Initialize Pygame Sound

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#_____Tkinter Configuration_____#

customtkinter.set_appearance_mode("dark") # Tkinter Dark Mode
customtkinter.set_default_color_theme("dark-blue") # Tkinter Theme
window = customtkinter.CTk() # Set Main Window

# Centre the Main Window
window_height = 300
window_width = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.iconbitmap("NEO.ico")
window.title('NEO Assistant')

FontLogin = Font(family="Mullish", size=14,)
MainFont = Font(family="Inter", size=12, weight = 'bold')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#_____Variables For Different Functions_____#

# Variables For Hover Effect (Main Option Screen)
A = 1
B = 1
C = 1
D = 1
E = 1

# Variables For Pomodoro Frame (ToDo Section)
V = 0 # Value used for going back & forth for Work - Break | 1 - 4
W = 2 # Value for changing the Background Frame images (Highlighted Clock etc.)
SF = 1 # (Save Frame) Value for saving the progress of pomo timer IF another section has been opened

# Variables For VPN Frame (Security Section)
SVPN = False # Speech VPN (Variable used when speech mode is used to turn VPN on)
SV = True # Switch Value

# Variable (Settings Section)
SET = True

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

def btn_clicked(): # Testing
    print("Button Clicked")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

def MainMenu():

    #_____MainMenu Window Configuration_____#

    window.configure(bg = "#151d33")
    Main = PhotoImage(file = f"GUI Images\\MainMenu.png")
    Main_Frame = Frame(window,bg = "#151d33",height = 270,width = 503,bd = 0,highlightthickness = 0,relief = "ridge", borderwidth = 0) # Main Frame
    Main_Frame.place(x = 82, y = 15)
    MainMenuu = Label(Main_Frame, bg = "#151d33", image = Main, highlightthickness = 0,relief = "ridge", borderwidth = 0)
    MainMenuu.pack()
    Main_Frame.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Task():

    global ToDo_Frame

    #_____All images for Task Section_____#

    # Sections Button Image (unhighlighted)
    To_Do_0 = PhotoImage(file = f"GUI Images\\To_Do_0.png")
    Timer_0 = PhotoImage(file = f"GUI Images\\Timer_0.png")
    # Sections Button Image (highlighted)
    To_Do_1 = PhotoImage(file = f"GUI Images\\To_Do_1.png")
    Timer_1 = PhotoImage(file = f"GUI Images\\Timer_1.png")
    # To-Do Frame Image
    ToDo_Main = PhotoImage(file = f"GUI Images\\To_Do_Main.png")
    ToDo_Entry_IMG = PhotoImage(file = f"GUI Images\\task_entry.png")
    ToDo_Del_IMG = PhotoImage(file = f"GUI Images\\task_del1.png")
    ToDo_Add_IMG = PhotoImage(file = f"GUI Images\\task_add1.png")
    Arrow_IMG = PhotoImage(file = f"GUI Images\\arrow.png") 
    Arrow1_IMG = PhotoImage(file = f"GUI Images\\arrow1.png")
    # Pomodoro Frame Image
    Pomodoro_IMG1 = PhotoImage(file = f"GUI Images\\pomodoro1.png")
    Pomodoro_IMG2 = PhotoImage(file = f"GUI Images\\pomodoro2.png")
    Pomodoro_IMG3 = PhotoImage(file = f"GUI Images\\pomodoro3.png")
    Pomodoro_IMG4 = PhotoImage(file = f"GUI Images\\pomodoro4.png")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #_____Main Frame____#

    window.configure(bg = "#151d33")
    MainFont_Clock = Font(family="DS-Digital", size=64, weight = 'bold')
    MainFont_Clock_Small = Font(family="DS-Digital", size=17, weight = 'bold')
    ToDo_BG_IMG = PhotoImage(file = f"GUI Images\\Task2.png")

    Task_Frame = Frame(window,bg = "#151d33",height = 270,width = 503,bd = 0,highlightthickness = 0,relief = "ridge", borderwidth = 0)
    Task_Frame.place(x = 82, y = 15)
    ToDo_BG = Label(Task_Frame, bg = "#151d33", image = ToDo_BG_IMG, highlightthickness = 0,relief = "ridge", borderwidth = 0)
    ToDo_BG.pack()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

    def Pomodoro(): # Pomodoro Section
        
        global V
        global W

        Timer_Button.configure(image = Timer_1) # Highlight Timer
        To_Do_Button.configure(image = To_Do_0) # UnHighlight To-Do

        #_____Pomodoro Window Configuration_____#

        Pomo_Frame = Frame(window,bg = "#151d33",height = 225,width = 503,bd = 0,highlightthickness = 0,relief = "ridge", borderwidth = 0)
        Pomo_Frame.place(x = 82, y = 60)
        Pomodoro_BG = Label(Pomo_Frame, bg = "#151d33", image = Pomodoro_IMG1, highlightthickness = 0,relief = "ridge", borderwidth = 0) # To-Do List Label (ToDo Background Image)
        Pomodoro_BG.place(x = 0, y = 0)

        Work_Text = Label(Pomo_Frame, bg = "#3D4560", text = 'Work 1/4',font = MainFont_Clock_Small, fg = '#ECECEC', highlightthickness = 0,relief = "ridge", borderwidth = 0)
        Work_Text.place(x = 9, y = 73,width = 86,height = 25)
        Break_Text = Label(Pomo_Frame, bg = "#3D4560", text = 'Break',font = MainFont_Clock_Small, fg = '#151d33', highlightthickness = 0,relief = "ridge", borderwidth = 0)
        Break_Text.place(x = 11, y = 113,width = 80,height = 24)

        # Default 25:00 Frame
        Min = Label(Pomo_Frame, bg = "#151d33", text = '25',font = MainFont_Clock, fg = '#ECECEC', highlightthickness = 0,relief = "ridge", borderwidth = 0)
        Min.place(x = 149, y = 62,width = 80,height = 60)
        Sec = Label(Pomo_Frame, bg = "#151d33", text = '00', font = MainFont_Clock, fg = '#ECECEC', highlightthickness = 0,relief = "ridge", borderwidth = 0)
        Sec.place(x = 280, y = 62,width = 80,height = 60)

        def Save(Minn, Secc, Work1, Breakk, Work2):
            Min.configure(text = Minn)
            Sec.configure(text = Secc)
            Work_Text.configure(fg = Work1) # Work text dark
            Break_Text.configure(fg = Breakk) # Break text light
            Work_Text.configure(text = Work2)
            Pomodoro_BG.configure(image = Pomodoro_IMG1)

        # So the label color, img etc. stays even after frame change
        if SF == 2: # Break 1
            Save('05','00','#151d33','#ECECEC','Work 1/4')
            Pomodoro_BG.configure(image = Pomodoro_IMG1)

        elif SF == 3: # Work 2
            Save('25','00','#ECECEC','#151d33','Work 2/4' )
            Pomodoro_BG.configure(image = Pomodoro_IMG2)

        elif SF == 4: # Break 2
            Save('05','00','#151d33','#ECECEC','Work 2/4')
            Pomodoro_BG.configure(image = Pomodoro_IMG2)
        
        elif SF == 5: # Work 3
            Save('25','00','#ECECEC','#151d33','Work 3/4' )
            Pomodoro_BG.configure(image = Pomodoro_IMG3)            
            
        elif SF == 6: # Break 3
            Save('05','00','#151d33','#ECECEC','Work 3/4')
            Pomodoro_BG.configure(image = Pomodoro_IMG3)

        elif SF == 7: # Work 4
            Save('25','00','#ECECEC','#151d33','Work 4/4' )
            Pomodoro_BG.configure(image = Pomodoro_IMG4)

        elif SF == 8: # Break 4
            Save('40','00','#151d33','#ECECEC','Work 4/4')
            Pomodoro_BG.configure(image = Pomodoro_IMG4)             

        def Timer_Start():
            global Thread_Value

            def WOW(): # Nested function so threading would work properly
                global V
                global W
                global SF
                global Thread_Value
        
                T1 = 00 # Seconds
                T2 = 25 # Minutes

                if V == 0: # Work 1-4
                    while T1 < 60:
                        Sec.configure(text = f"{T1:02}") # Change seconds text
                        Min.configure(text = f"{T2:02}") # Change minutes text
                        T1 = T1 - 1 # Seconds countdown -1

                        if Thread_Value == True:
                            pass
                        else:
                            Min.configure(text = '25')
                            Sec.configure(text = '00')
                            Work_Text.configure(fg = '#ECECEC') # Work text light
                            Break_Text.configure(fg = '#151d33') # Break text Dark
                            Work_Text.configure(text = 'Work 1/4')
                            Pomodoro_BG.configure(image = Pomodoro_IMG1)
                            break

                        if T1 < 0: # if 60 seconds pass reduce minute by 1
                            T2 -= 1
                            T1 = 59
                        elif T2 < 0 and W !=5 : # Break
                            print('Break ' + str(W))
                            T2 = 5
                            T1 = 00
                            V = 1
                            SF += 1
                            Sec.configure(text = f"{T1:02}")
                            Min.configure(text = f"{T2:02}")
                            Work_Text.configure(fg = '#151d33') # Work text dark
                            Break_Text.configure(fg = '#ECECEC') # Break text light
                            break
                        elif T2 < 0 and W == 5:
                            print('Last Break')
                            T2 = 40
                            T1 = 00
                            V = 2
                            Sec.configure(text = f"{T1:02}")
                            Min.configure(text = f"{T2:02}")                            
                            Work_Text.configure(fg = '#151d33') # Work text dark
                            Break_Text.configure(fg = '#ECECEC') # Break text light
                            break

                        if T1 == -2 or T2 == -2: # To stop when the timer reaches a negative number
                            break
                        
                        Sec.update() # update the frame
                        time.sleep(1)

                elif V == 1: # 5 min Break
                    T1 = 00 # Seconds
                    T2 = 5 # Minutes
                    while T1 < 60:
                        Sec.configure(text = f"{T1:02}") # Change seconds text
                        Min.configure(text = f"{T2:02}") # Change minutes text
                        T1 = T1 - 1 # Seconds countdown -1

                        if T1 <= 0: # if 60 seconds pass reduce minute by 1
                            T2 -= 1
                            T1 = 59
                        elif T2 < 0:
                            T2 = 25
                            T1 = 00
                            V = 0
                            SF += 1
                            Sec.configure(text = f"{T1:02}")
                            Min.configure(text = f"{T2:02}")
                            Work_Text.configure(fg = '#ECECEC') # Work text dark
                            Break_Text.configure(fg = '#151d33') # Break text light
                            print('Work ' + str(W) + ' Change text and background IMG')
                            if W == 2:
                                Work_Text.configure(text = 'Work 2/4')
                                Pomodoro_BG.configure(image = Pomodoro_IMG2)
                            elif W == 3:
                                Work_Text.configure(text = 'Work 3/4')
                                Pomodoro_BG.configure(image = Pomodoro_IMG3)
                            elif W == 4:
                                Work_Text.configure(text = 'Work 4/4')
                                Pomodoro_BG.configure(image = Pomodoro_IMG4)
                            print('Break ' + str(W) + ' is done')
                            W += 1
                            break

                        if T1 == -2 or T2 == -2: # To stop when the timer reaches a negative number
                            break

                        Sec.update() # update the frame
                        time.sleep(1)

                elif V == 2: # Last 40 min break
                    print('40 min Break')
                    T1 = 00 # Seconds
                    T2 = 40 # Minutes
                    while T1 < 60:
                        Sec.configure(text = f"{T1:02}") # Change seconds text
                        Min.configure(text = f"{T2:02}") # Change minutes text
                        T1 = T1 - 1 # Seconds countdown -1

                        if T1 <= 0: # if 60 seconds pass reduce minute by 1
                            T2 -= 1
                            T1 = 59
                        elif T2 < 0:
                            T2 = 25
                            T1 = 00
                            V = 0
                            W = 1
                            SF = 1
                            Sec.configure(text = f"{T1:02}")
                            Min.configure(text = f"{T2:02}")
                            Work_Text.configure(fg = '#ECECEC') # Work text dark
                            Break_Text.configure(fg = '#151d33') # Break text light

                            Work_Text.configure(text = 'Work 1/4')
                            Pomodoro_BG.configure(image = Pomodoro_IMG1)
                            break

                        Sec.update() # update the frame
                        time.sleep(1)

            Thread_Value = True

            Thread = threading.Thread(target=WOW)
            Thread.start()

        def Thread_Stop():
            global Thread_Value
            Thread_Value = False

        Reset_Btn_IMG = PhotoImage(file = f"GUI Images\\reset_btn.png")
        Reset_Btn = Button(image = Reset_Btn_IMG,borderwidth = 0,highlightthickness = 0,command = Thread_Stop, activebackground= '#151D33', relief = "flat")
        Reset_Btn.place(x = 346, y = 196,width = 55,height = 30)

        Play_Btn_IMG = PhotoImage(file = f"GUI Images\\play_btn.png")
        Play_Btn = Button(image = Play_Btn_IMG,borderwidth = 0,highlightthickness = 0,command = Timer_Start,activebackground= '#151D33', relief = "flat")
        Play_Btn.place(x = 267, y = 196,width = 54,height = 30)

        Pomo_Frame.mainloop()
        Task_Frame.mainloop()

    def Todo(): # To Do Section

        global task_entry
        global ToDo_Frame
        global List

        Timer_Button.configure(image = Timer_0) # UnHighlight Timer
        To_Do_Button.configure(image = To_Do_1) # Highlight To-Do

        #_____Todo Frame_____#

        ToDo_Frame = Frame(window,bg = "#151d33",height = 227,width = 503,bd = 0,highlightthickness = 0,relief = "ridge", borderwidth = 0)
        ToDo_Frame.place(x = 82, y = 58)
        ToDo_BG = Label(ToDo_Frame, bg = "#151d33", image = ToDo_Main, highlightthickness = 0,relief = "ridge", borderwidth = 0)
        ToDo_BG.pack()

        #_____ADD & DEL Functions_____#

        def list_validation(): # Validate if Items are Duplicated & To Delete Empty Rows (bug) etc.

            # Delete Empty Rows Appearing After Button Press
            output=""
            with open("Sample Files\\Note_Text\\NoteTXT.txt") as f:
                for line in f:
                    if not line.isspace():
                        output+=line
                        
            f = open("Sample Files\\Note_Text\\NoteTXT.txt","w")
            f.write(output)
            f.close()

            # Duplicate Item Validation
            NoteTXT = open('Sample Files\\Note_Text\\NoteTXT.txt', 'r')
            data2 = NoteTXT.readlines()
            to_add = task_entry.get()

            X = 0
            for line in data2:
                line = line.strip('\n')
                if line.strip(' - ') == to_add:
                    X = X + 1
                    task_entry.configure(fg="red")
                    task_entry.delete(0, END)
                    task_entry.insert(END,"Duplicate Item Found")
                    task_entry.update()
                    time.sleep(1)
                    task_entry.configure(fg="black")
                    task_entry.delete(0, END)
                    break

        def add_item(): # Add Items To The List
            global task_entry
            global List

            list_validation()
            
            to_add = task_entry.get()
            X = 0

            # Add item to the text file
            if to_add != "" and X == 0:
                with open('Sample Files\\Note_Text\\NoteTXT.txt', 'a') as file:
                    file.write('\n - ' + to_add.rstrip())

            # Add item to the ListBox
                to_add2 = ' - ' + task_entry.get()
                List.insert(END, to_add2)
                task_entry.delete(0, END)
                task_entry.insert(0,"")
                task_entry.update()
            
            if List.size() > 7:
                Arrow1.configure(image = Arrow_IMG)
            
            List.update()

        def delete_item(): # Delete Items On The List

            global List

            list_validation()

            NoteTXT = open('Sample Files\\Note_Text\\NoteTXT.txt', 'r')
            data2 = NoteTXT.readlines()

            # Delete item from the text file
            selected = List.get(ANCHOR)

            with open("Sample Files\\Note_Text\\NoteTXT.txt", "w") as file:
                for line in data2:
                    if line.strip("\n") != selected.rstrip():
                        file.write(line)

            # Delete item to the ListBox
            List.delete(ANCHOR)

            if List.size() < 8:
                Arrow1.configure(image = Arrow1_IMG)

            List.update()

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------#

        # EntryBox
        task_entry = Entry(bd = 0,bg = "#ececec",highlightthickness = 0,font=MainFont)
        task_entry.place(x = 102.0, y = 246,width = 334,height = 26)

        # Delete Button
        delete_button = Button(image = ToDo_Del_IMG,borderwidth = 0,highlightthickness = 0,command = delete_item,activebackground= '#1E2746',relief = "flat")
        delete_button.place(x = 518, y = 242,width = 54,height = 30)

        # Add Button
        add_button = Button(image = ToDo_Add_IMG,borderwidth = 0,highlightthickness = 0,command = add_item,activebackground= '#1E2746',relief = "flat")
        add_button.place(x = 455, y = 242,width = 54,height = 30)

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------#

        # Item ListBox
        List = Listbox(ToDo_Frame, font=MainFont, width = 52, height = 7, bd = 0, bg="#ECECEC", highlightthickness = 0, selectbackground = '#a6a6a6', selectforeground= '#000000', activestyle = NONE)
        List.place(x = 17, y = 15)

        list_validation()

        # Arrow
        Arrow1 = Label(ToDo_Frame, image = Arrow1_IMG, bd = 0, highlightthickness = 0,relief = "ridge", borderwidth = 0)
        Arrow1.place(x = 240, y = 156)

        # Entry Rounded Image
        ToDo_Entry = Label(ToDo_Frame, bg = "#000000", image = ToDo_Entry_IMG, highlightthickness = 0,relief = "ridge", borderwidth = 0)
        ToDo_Entry.place(x = 16, y =187)

        # Scroll Bar
        Scroll = Scrollbar(ToDo_Frame)
        Scroll.place(x = 470, y = 10, height = 150)
        List.config(yscrollcommand=Scroll.set)
        Scroll.config(command=List.yview)

        # Opening & Inserting textfile contents into ListBox
        NoteTXT = open('Sample Files\\Note_Text\\NoteTXT.txt', 'r')
        data = NoteTXT.readlines()
        for item in data: 
            List.insert(END,item)

        if List.size() > 7:
            Arrow1.configure(image = Arrow_IMG)

        keyboard.add_hotkey('Return', add_item)
        keyboard.add_hotkey('Delete', delete_item)
        
        List.update()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #_____To-Do, Timer, QR to Link Section Buttons_____#

    Timer_Button = Button(image = Timer_0,borderwidth = 0,highlightthickness = 0,command = Pomodoro,activebackground= '#1E2746',relief = "flat")
    Timer_Button.place(x = 321, y = 27,width = 70,height = 22)

    To_Do_Button = Button(image = To_Do_1,borderwidth = 0,highlightthickness = 0,command = Todo,activebackground= '#1E2746',relief = "flat")
    To_Do_Button.place(x = 214, y = 27,width = 70,height = 22)

    Todo() # starting frame is the Todo List

    Task_Frame.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Security():

    #_____All images for Security Section_____#

    # Security Sections Button Image (unhighlighted)
    VPN_0 = PhotoImage(file = f"GUI Images\\VPN_0.png")
    Encryptor_0 = PhotoImage(file = f"GUI Images\\Encryptor_0.png")
    Scanner_0 = PhotoImage(file = f"GUI Images\\Scanner_0.png")

    # Security Sections Button Image (highlighted)
    VPN_1 = PhotoImage(file = f"GUI Images\\VPN_1.png")
    Encryptor_1 = PhotoImage(file = f"GUI Images\\Encryptor_1.png")
    Scanner_1 = PhotoImage(file = f"GUI Images\\Scanner_1.png")

    Padlock_IMG = PhotoImage(f"GUI Images\\Pad.png") # Padlock IMG

    Security_Main_IMG = PhotoImage(file = f"GUI Images\\Security.png") # VPN Background Main
    Security_OFF_IMG = PhotoImage(file = f"GUI Images\\Security1.png") # VPN Background OFF
    Security_ON_IMG = PhotoImage(file = f"GUI Images\\Security2.png") # VPN Background ON

    OFF_IMG = PhotoImage(file = f"GUI Images\\OFF.png") # VPN OFF Button
    ON_IMG = PhotoImage(file = f"GUI Images\\ON.png") # VPN OFF Button

    Encryptor_BG_IMG = PhotoImage(file = f"GUI Images\\Encryptor_BG.png")
    Encryptor_BG1_IMG = PhotoImage(file = f"GUI Images\\Encryptor_BG1.png")
    Encryptor_BG2_IMG = PhotoImage(file = f"GUI Images\\Encryptor_BG2.png")

    GenerateKey_IMG = PhotoImage(file = f"GUI Images\\GenerateKey.png")
    Encrypt_IMG = PhotoImage(file = f"GUI Images\\Encrypt.png")
    Decrypt_IMG = PhotoImage(file = f"GUI Images\\Decrypt.png")
    DotKey_IMG = PhotoImage(file = f"GUI Images\\DotKey.png")
    DotTXT_IMG = PhotoImage(file = f"GUI Images\\DotTXT.png")

    Scanner_BG_IMG = PhotoImage(file = f"GUI Images\\Scanner_BG.png")
    Scanner_BG_IMG_1 = PhotoImage(file = f"GUI Images\\Scanner_BG_1.png")
    Scan_BTN = PhotoImage(file = f"GUI Images\\Scan_BTN.png")
    Select_BTN = PhotoImage(file = f"GUI Images\\Select_BTN.png")
    URL_Good = PhotoImage(file = f"GUI Images\\URL_Good.png")
    File_Good = PhotoImage(file = f"GUI Images\\File_Good.png")
    Error_Bad = PhotoImage(file = f"GUI Images\\Error_Bad.png")
    Back_IMG = PhotoImage(file = f"GUI Images\\Back.png")
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #_____Main Frame____#

    window.configure(bg = "#151d33")

    Security_Frame = Frame(window,bg = "#151d33",height = 270,width = 503,bd = 0,highlightthickness = 0,relief = "ridge", borderwidth = 0) # Security Frame
    Security_Frame.place(x = 82, y = 15)
    Sec = Label(Security_Frame, bg = "#151d33", image = Security_Main_IMG, highlightthickness = 0,relief = "ridge", borderwidth = 0)
    Sec.pack()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#   

    #_____VPN, Encryptor/Decryptor & File/URL Scanner Sections____#

    def VPN():
        global SV # Switch Value
        global SVPN # Speech VPN (Variable used when speech mode is used to turn VPN on)

        VPN_Button.configure(image = VPN_1)
        Encryptor_Button.configure(image = Encryptor_0)
        Scanner_Button.configure(image = Scanner_0)

        VPN_Frame = Frame(window,bg = "#151d33",height = 235,width = 503,bd = 0,highlightthickness = 0,relief = "ridge", borderwidth = 0)
        VPN_Frame.place(x = 82, y = 50)
        Sec1 = Label(VPN_Frame, bg = "#151d33", image = Security_OFF_IMG, highlightthickness = 0,relief = "ridge", borderwidth = 0)
        Sec1.pack()

        #----------------------------------------------------------------------------------------------------------------------------------------------------------------#   

        def ON():
            global SV # Switch Value
            global SVPN # Speech VPN (Variable used when speech mode is used to turn VPN on)

            if SV == True:
                Switch.configure(image = ON_IMG)
                Sec1.configure(image = Security_ON_IMG)
                subprocess.call('C://Program Files//OpenVPN Connect//OpenVPNConnect.exe')
                X = 0
                while X < 1: # Wait until OpenVPN is fully loaded so the ON button can be located
                    SWITCH = pg.locateOnScreen('Image Recognition\\Switch.png',grayscale=True, confidence=0.8)
                    if SWITCH != None:
                        pg.click(SWITCH)
                        X = 1
                    else:
                        time.sleep(1)
                        continue
                    time.sleep(1)
                pg.hotkey('win', 'down')
                SV = False
            elif SV == False:
                Switch.configure(image = OFF_IMG)
                Sec1.configure(image = Security_OFF_IMG)
                subprocess.call('C://Program Files//OpenVPN Connect//OpenVPNConnect.exe')
                X = 0
                while X < 1: # Wait until OpenVPN is fully loaded so the ON button can be located
                    SWITCH = pg.locateOnScreen('Image Recognition\\Switch2.png',grayscale=True, confidence=0.8)
                    if SWITCH != None:
                        pg.click(SWITCH)
                        X = 1
                    else:
                        time.sleep(1)
                        continue
                    time.sleep(1)
                pg.hotkey('win', 'down')
                SV = True

        Switch = Button(image = OFF_IMG,borderwidth = 0,highlightthickness = 0,command = ON,activebackground= '#1F2D42',relief = "flat")
        Switch.place(x = 181, y = 195, width = 60, height = 32)

        #----------------------------------------------------------------------------------------------------------------------------------------------------------------#   

        if SV == False: # (Save Frame) For VPN frame to show ON when navigating to another section
            Switch.configure(image = ON_IMG)
            Sec1.configure(image = Security_ON_IMG)
        elif SV == True:
            pass

        if SVPN == True: # Speech Mode activating VPN
            ON()
            SVPN = False
        else:
            pass

        VPN_Frame.mainloop()

    def Encryptor():
        global data1
        global data2
        global TXT_AND_KEY
        global Encryptor_Frame
        global GenerateKey_Button

        VPN_Button.configure(image = VPN_0)
        Encryptor_Button.configure(image = Encryptor_1)
        Scanner_Button.configure(image = Scanner_0)

        # 128-bits, AES128 Encryption (UTF 8 Encoding)

        path = f"Sample Files\\Generated_Key"
        dir_list = os.listdir(path)

        if len(dir_list) == 0:
            Encryptor_Frame = Frame(window,bg = "#151d33",height = 270,width = 503,bd = 0,highlightthickness = 0,relief = "ridge", borderwidth = 0) # Encryptor Frame
            Encryptor_Frame.place(x = 82, y = 50)
            Enc = Label(Encryptor_Frame, bg = "#151d33", image = Encryptor_BG_IMG, highlightthickness = 0,relief = "ridge", borderwidth = 0)
            Enc.pack()
        else:
            Encryptor_Frame = Frame(window,bg = "#151d33",height = 270,width = 503,bd = 0,highlightthickness = 0,relief = "ridge", borderwidth = 0) # Encryptor Frame
            Encryptor_Frame.place(x = 82, y = 50)
            Enc = Label(Encryptor_Frame, bg = "#151d33", image = Encryptor_BG1_IMG, highlightthickness = 0,relief = "ridge", borderwidth = 0)
            Enc.pack()

        def Generate():
            key = Fernet.generate_key() # Generate Key

            with open(os.path.join('Sample Files\\Generated_Key','keygen.key'),'wb')as mykey: # Save Generated Key
               mykey.write(key)

            Enc.configure(image = Encryptor_BG1_IMG)
    
        TXT_AND_KEY =  0 # Variable used to determine & display a tick if both txt and key files are imported (if 2 = both files have been imported)

        def DotKey():
            global TXT_AND_KEY
            global data1
            try:
                DotKeyName = filedialog.askopenfilename(initialdir="Sample Files\\Generated_Key\\",title="Select A File", filetypes=(("key", "*.key"), ("all files", "*.*")))
                seed1 = open(DotKeyName, 'rb')
                data1 = seed1.read()
                print(data1)
                TXT_AND_KEY += 1

                if TXT_AND_KEY == 2:
                    Enc.configure(image = Encryptor_BG2_IMG)
            except:
                pass

        def DotTXT():
            global TXT_AND_KEY
            global data2
            try:
                DotTXT = filedialog.askopenfilename(initialdir="Sample Files\\Secret_Text\\\\",title="Select A File", filetypes=(("text", "*.txt"), ("all files", "*.*")))
                seed2 = open(DotTXT, 'rb')
                data2 = seed2.read()
                print(data2)
                TXT_AND_KEY += 1

                if TXT_AND_KEY == 2:
                    Enc.configure(image = Encryptor_BG2_IMG)
            except:
                pass                     
        
        def Encrypt():
            global data1 # Key File
            global data2 # TXT File
            global TXT_AND_KEY

            path = f"Sample Files\\Secret_Text\\" # Path to save file

            try:
                if TXT_AND_KEY == 2:
                    f = Fernet(data1)
                    encryptedData = f.encrypt(data2)
                    with open(os.path.join('Sample Files\\Secret_Text\\', 'SecretEncrypted.txt'),'wb') as SecretEncrypted: # Save Encrypted File
                        SecretEncrypted.write(encryptedData)
                    TXT_AND_KEY = 0
            except:
                pass
            
            window.update()

        def Decrypt():
            global data1 # Key File
            global data2 # TXT File
            global TXT_AND_KEY

            try:
                if TXT_AND_KEY == 2:
                    f = Fernet(data1) # Utilize the Key
                    decryptedData = f.decrypt(data2) # Encrypt the Data
                    with open(os.path.join('Sample Files\\Secret_Text\\', 'SecretDecrypted.txt'),'wb') as SecretDecrypted: # Save Encrypted File
                        SecretDecrypted.write(decryptedData)
                    TXT_AND_KEY = 0
            except:
                pass

            window.update()

        GenerateKey_Button = Button(image = GenerateKey_IMG,borderwidth = 0,highlightthickness = 0,command = Generate,activebackground= '#151D33',relief = "flat")
        GenerateKey_Button.place(x = 269, y = 66,width = 129,height = 34)

        DotKey_Button = Button(image = DotKey_IMG,borderwidth = 0,highlightthickness = 0,command = DotKey,activebackground= '#151D33',relief = "flat")
        DotKey_Button.place(x = 195, y = 125,width = 80,height = 80)

        DotTXT_Button = Button(image = DotTXT_IMG,borderwidth = 0,highlightthickness = 0,command = DotTXT,activebackground= '#151D33',relief = "flat")
        DotTXT_Button.place(x = 393, y = 125,width = 80,height = 80)

        Encrypt_Button = Button(image = Encrypt_IMG,borderwidth = 0,highlightthickness = 0,command = Encrypt,activebackground= '#151D33',relief = "flat")
        Encrypt_Button.place(x = 185, y = 231,width = 100,height = 34)

        Decrypt_Button = Button(image = Decrypt_IMG,borderwidth = 0,highlightthickness = 0,command = Decrypt,activebackground= '#151D33',relief = "flat")
        Decrypt_Button.place(x = 383, y = 231,width = 100,height = 34)

        Encryptor_Frame.mainloop()

    def Scanner():
        # DONE WITH THE HELP OF VIRUS TOTAL API DOCUMENTATION

        global MainFont
        global urlscan_entry
        global scanned_file

        VPN_Button.configure(image = VPN_0)
        Encryptor_Button.configure(image = Encryptor_0)
        Scanner_Button.configure(image = Scanner_1)

        Scanner_Frame = Frame(window,bg = "#151d33",height = 235,width = 503,bd = 0,highlightthickness = 0,relief = "ridge", borderwidth = 0) # Encryptor Frame
        Scanner_Frame.place(x = 82, y = 50)
        Scan = Label(Scanner_Frame, bg = "#151d33", image = Scanner_BG_IMG, highlightthickness = 0,relief = "ridge", borderwidth = 0)
        Scan.pack()

        def Good_Widget(A):
            global Good_Frame

            def back():
                Good_Frame.destroy()
                Back.destroy()

            Good_Frame = Frame(window,bg = "#151d33",height = 235,width = 503,bd = 0,highlightthickness = 0,relief = "ridge", borderwidth = 0) # Encryptor Frame
            Good_Frame.place(x = 82, y = 50)

            if A == '1':
                Good = Label(Good_Frame, bg = "#151d33", image = URL_Good, highlightthickness = 0,relief = "ridge", borderwidth = 0)
                Good.pack()
            elif A == '2':
                Bad = Label(Good_Frame, bg = "#151d33", image = File_Good, highlightthickness = 0,relief = "ridge", borderwidth = 0)
                Bad.pack()
            elif A == '3':
                Error = Label(Good_Frame, bg = "#151d33", image = Error_Bad, highlightthickness = 0,relief = "ridge", borderwidth = 0)
                Error.pack()
            else:
                pass               

            Back = Button(image = Back_IMG,borderwidth = 0,highlightthickness = 0,command = back,relief = "flat", activebackground = '#151D33')
            Back.place(x = 243, y = 221,width = 182,height = 34)

            Good_Frame.mainloop()

        def SCAN(): # Scan either URL or File
            global urlscan_entry

            if urlscan_entry.get() == '':
                FILE_Scan()
            else:
                URL_Scan()

        def FILE_Select(): # Choose the specific file to be scanned
            global scanned_file
            scan_file = filedialog.askopenfilename(initialdir="C:\\",title="Select A File", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
            scanned_file = open(scan_file, 'rb')

            Scan.configure(image = Scanner_BG_IMG_1) # Tick becomes green

        def FILE_Scan(): # Scan the File Imported
            global scanned_file

            url = "https://www.virustotal.com/api/v3/files"

            try:
                files = {"file": scanned_file}

                headers = {
                    "Accept": "application/json",
                    "x-apikey": "3f361951cb29469873e06f132088b9d81f478afc5d46dd1b26f9ba4525d0e857"
                }

                response1 = requests.post(url, files=files, headers=headers) # Initiating the API connection with parameters (Headers)
                decodedResponse1 = json.loads(response1.text) # Convert into json format
                hash_id = (decodedResponse1["data"]["id"]) # Getting Hash ID for File

                url = "https://www.virustotal.com/api/v3/analyses/" + hash_id

                response2 = requests.get(url, headers=headers)
                decodedResponse2 = json.loads(response2.text)

                main_check = (decodedResponse2["data"]["attributes"]["stats"])
                suspicious_check_int = int(main_check["suspicious"])
                suspicious_check_str = str(main_check["suspicious"])
                malicious_check_int = int(main_check["malicious"])
                malicious_check_str = str(main_check["malicious"])
                # undetected_int = int(main_check["undetected"])
                # undetected_str = str(main_check["undetected"])
                total_check = suspicious_check_int + malicious_check_int

                if suspicious_check_int > malicious_check_int & suspicious_check_int > 0: 
                    messagee = 'The URL provided was rated as \'Suspicious\' by ' + suspicious_check_str + ' Engines.'
                    messagebox.showwarning(title = 'Scan Complete', message = messagee)

                elif suspicious_check_int < malicious_check_int & malicious_check_int > 0:
                    messagee = 'The URL provided was rated as \'Malicious\' by ' + malicious_check_str + ' Engines.'
                    messagebox.showwarning(title = 'Scan Complete', message = messagee)

                elif suspicious_check_int == malicious_check_int & total_check > 0:
                    total_eng = suspicious_check_int + malicious_check_int
                    messagee = 'The URL provided was rated as both \'Malicious\' and \'Suspicious\' by ' + total_eng + ' Engines.'
                    messagebox.showwarning(title = 'Scan Complete', message = messagee)

                else:
                    Good_Widget('2')

            except:
                Good_Widget('3')
        
        def URL_Scan(): # # Scan the URL Pasted
            global urlscan_entry
            global Good_Frame

            # user input, ip or url, to be submitted for a url analysis stored in the target_url variable
            target_url = urlscan_entry.get()

            # For a url analysis report virustotal requires the "URL identifier" or base64 representation of URL to scan (w/o padding)

            try:
                # create virustotal "url identifier" from user input stored in target_url
                # Encode the user submitted url to base64 and strip the "==" from the end
                url_id = base64.urlsafe_b64encode(target_url.encode()).decode().strip("=")

                # amend the virustotal apiv3 url to include the unique generated url_id
                url = "https://www.virustotal.com/api/v3/urls/" + url_id

                API_KEY = '3f361951cb29469873e06f132088b9d81f478afc5d46dd1b26f9ba4525d0e857'

                headers = {
                    "Accept": "application/json",
                    "x-apikey": API_KEY
                }

                response = requests.request("GET", url, headers=headers)

                # load returned json from virustotal into a python dictionary called decodedResponse
                decodedResponse = json.loads(response.text)

                dict_web = decodedResponse["data"]["attributes"]["last_analysis_results"]
                tot_engine_c = 0
                tot_detect_c = 0
                result_eng = []
                eng_name = []
                count_harmless = 0
                for i in dict_web:
                    tot_engine_c - 1 + tot_engine_c
                    if dict_web[i]["category"] == "malicious" or dict_web[i]["category"] == "suspicious":
                        result_eng.append(dict_web[i]["result"])
                        eng_name.append(dict_web[i]["engine_name"])
                        tot_detect_c - 1 + tot_detect_c
                res = []

                for i in result_eng:
                    if i not in res:
                        res.append(i)
                result_eng = res

                if tot_detect_c > 0:
                    messagee = "The URL provied was rated for " + str(result_eng)[1:-1] + " on " + str(tot_detect_c) + " engines out of "+ str(tot_engine_c)
                    messagebox.showwarning(title = 'Scan Complete', message = messagee)
                else:
                    Good_Widget('1')

            except:
                Good_Widget('3')

        urlscan_entry = Entry(bd = 0,bg = "#ececec",highlightthickness = 0,font=MainFont)
        urlscan_entry.place(x = 162.0, y = 79,width = 387.0,height = 24)

        Scan_Purple_BTN = Button(image = Scan_BTN,borderwidth = 0,highlightthickness = 0,command = SCAN,activebackground= '#151D33',relief = "flat")
        Scan_Purple_BTN.place(x = 243, y = 221,width = 182,height = 34)

        Select_Purple_BTN = Button(image = Select_BTN,borderwidth = 0,highlightthickness = 0,command = FILE_Select,activebackground= '#151D33',relief = "flat")
        Select_Purple_BTN.place(x = 243, y = 142,width = 182,height = 34)

        Scanner_Frame.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #_____VPN, Encryptor/Decryptor & File/URL Scanner Buttons_____#

    VPN_Button = Button(image = VPN_1,borderwidth = 0,highlightthickness = 0,command = VPN,activebackground= '#1E2746',relief = "flat")
    VPN_Button.place(x = 236, y = 23,width = 75,height = 28)

    Encryptor_Button = Button(image = Encryptor_0,borderwidth = 0,highlightthickness = 0,command = Encryptor,activebackground= '#1E2746',relief = "flat")
    Encryptor_Button.place(x = 333, y = 23,width = 97,height = 28)

    Scanner_Button = Button(image = Scanner_0,borderwidth = 0,highlightthickness = 0,command = Scanner,activebackground= '#1E2746',relief = "flat")
    Scanner_Button.place(x = 452, y = 23,width = 97,height = 28)

    Padlock_Button = Button(image = Padlock_IMG, command = VPN, borderwidth = 0)
    Padlock_Button.place(x = 200, y = 200)

    VPN() # starting frame is the VPN List

    Security_Frame.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Settings():
    global window
    global SET

    if SET == True:
        window.geometry("1200x600")
        SET = False
    elif SET == False:
        window.geometry("600x300")
        SET = True
    window.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Speech():

    def Speechh():
        global SV # Switch Value
        global SVPN # Speech VPN (Variable used when speech mode is used to turn VPN on)
        global window

        recognizer = speech_recognition.Recognizer()

        pygame.mixer.init()
        Listen = pygame.mixer.Sound("Sound\\Listen.wav")
        Listen.set_volume(0.5)
        Listen.play()
        
        while True:

            try:  

                with speech_recognition.Microphone() as mic:

                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recognizer.listen(mic)

                    text = recognizer.recognize_google(audio)
                    text = text.lower()

                    print(f"{text}")

                    if text == "on vpn":
                        SVPN = True
                        SV = True
                        Listen = pygame.mixer.Sound("Sound\\Work.wav")
                        Listen.set_volume(0.5)
                        Listen.play()
                        Security()
                    elif text == "off vpn":
                        SVPN = True
                        SV = False
                        Listen = pygame.mixer.Sound("Sound\\Work.wav")
                        Listen.set_volume(0.5)
                        Listen.play()
                        Security()
                    else:
                        Listen = pygame.mixer.Sound("Sound\\NoWork.wav")
                        Listen.set_volume(0.5)
                        Listen.play()
                
                break

            except:
                break

            # except speech_recognition.UnknownValueError():

            #     recognizer =  speech_recognition.Recognizer()
            #     continue

    Thread = threading.Thread(target=Speechh)
    Thread.start()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

def MainWindow():
    global window

    #_____Master Window Configuration_____#

    window.geometry("600x300")
    window.configure(bg = "#020b1f")
    canvas = Canvas(
        window,
        bg = "#020b1f",
        height = 300,
        width = 600,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    MainWindow_img1 = PhotoImage(file = f"GUI Images\\MainWindow.png")
    MainWindow = canvas.create_image(
        300.0, 150.0,
        image=MainWindow_img1)

    HHimg0 = PhotoImage(file = f"GUI Images\\HHimg0.png") # For Hover Button 0 (Mic)
    HHimg1 = PhotoImage(file = f"GUI Images\\HHimg1.png") # For Hover Button 1 (Settings)
    HHimg2 = PhotoImage(file = f"GUI Images\\HHimg2.png") # For Hover Button 2 (Security)
    HHimg3 = PhotoImage(file = f"GUI Images\\HHimg3.png") # For Hover Button 3 (Task)
    HHimg4 = PhotoImage(file = f"GUI Images\\HHimg4.png") # For Hover Button 4 (Main Menu)

    Himg0 = PhotoImage(file = f"GUI Images\\Himg0.png") # For Pressed Button 0 (Mic)
    Himg1 = PhotoImage(file = f"GUI Images\\Himg1.png") # For Pressed Button 1 (Settings)
    Himg2 = PhotoImage(file = f"GUI Images\\Himg2.png") # For Pressed Button 2 (Security)
    Himg3 = PhotoImage(file = f"GUI Images\\Himg3.png") # For Pressed Button 3 (Task)
    Himg4 = PhotoImage(file = f"GUI Images\\Himg4.png") # For Pressed Button 4 (Main Menu)

    img0 = PhotoImage(file = f"GUI Images\\img0.png") # For Main Button 0 (Mic)
    img1 = PhotoImage(file = f"GUI Images\\img1.png") # For Main Button 1 (Settings)
    img2 = PhotoImage(file = f"GUI Images\\img2.png") # For Main Button 2 (Security)
    img3 = PhotoImage(file = f"GUI Images\\img3.png") # For Main Button 3 (Task)
    img4 = PhotoImage(file = f"GUI Images\\img4.png") # For Main Button 4 (Main Menu)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Button 0 (Mic Button)

    def onButton0(X): # Hover Effect On
        global A
        if A == 1:        
            Mic_Button['image'] = HHimg0
            
    def leaveButton0(X): # Hover Effect Off
        global A
        if A == 1:
            Mic_Button['image'] = img0

    def Pressed0(): # Button Press (Using Voice Command)
        Mic_Button.configure(image = Himg0)
        print("Listening...")
        Speech()
        time.sleep(4)
        Mic_Button.configure(image = img0) 

    Mic_Button = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = Speech,activebackground='#151D33',relief = "flat")
    Mic_Button.place(x = 16, y = 234,width = 52,height = 52)

    Mic_Button.bind('<Enter>',onButton0)
    Mic_Button.bind('<Leave>',leaveButton0)
    keyboard.add_hotkey('V', Pressed0)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Button 1 (Settings Button)

    def onButton1(X): # Hover Effect On
        global B
        if B == 1:        
            Settings_Button['image'] = HHimg1

    def leaveButton1(X): # Hover Effect Off
        global B
        if B == 1:
            Settings_Button['image'] = img1

    def Pressed1(X): # Button Press

        Mic_Button.configure(image = img0)   
        Settings_Button.configure(image = Himg1)   
        Security_Button.configure(image = img2)   
        Task_Button.configure(image = img3)   
        MainMenu_Button.configure(image = img4)
        global A
        global B
        global C
        global D
        global E
        A = 1
        B = B + 1        
        C = 1
        D = 1
        E = 1

    Settings_Button = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = Settings,activebackground='#151D33',relief = "flat")
    Settings_Button.place(x = 16, y = 183,width = 52,height = 42)
 
    Settings_Button.bind ('<Enter>',onButton1)
    Settings_Button.bind('<Leave>',leaveButton1)
    Settings_Button.bind ('<Button>',Pressed1)
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Button 2 (Security Button)

    def onButton2(X): # Hover Effect On
        global C
        if C == 1:        
            Security_Button['image'] = HHimg2

    def leaveButton2(X): # Hover Effect Off
        global C
        if C == 1:
            Security_Button['image'] = img2

    def Pressed2(X): # Button Press

        Mic_Button.configure(image = img0)   
        Settings_Button.configure(image = img1)   
        Security_Button.configure(image = Himg2)   
        Task_Button.configure(image = img3)   
        MainMenu_Button.configure(image = img4)            
        global A
        global B
        global C
        global D
        global E
        A = 1
        B = 1
        C = C + 1
        D = 1
        E = 1

    Security_Button = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = Security,activebackground='#151D33',relief = "flat")
    Security_Button.place(x = 16, y = 143,width = 52,height = 42)

    Security_Button.bind ('<Enter>',onButton2)
    Security_Button.bind('<Leave>',leaveButton2)
    Security_Button.bind ('<Button>',Pressed2)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    # Button 3 (Task Button)   

    def onButton3(X): # Hover Effect On
        global D
        if D == 1:        
            Task_Button['image'] = HHimg3

    def leaveButton3(X): # Hover Effect Off
        global D
        if D == 1:
            Task_Button['image'] = img3

    def Pressed3(X): # Button Press

        Mic_Button.configure(image = img0)   
        Settings_Button.configure(image = img1)   
        Security_Button.configure(image = img2)   
        Task_Button.configure(image = Himg3)   
        MainMenu_Button.configure(image = img4)  
        global A
        global B
        global C
        global D
        global E
        A = 1
        B = 1
        C = 1
        D = D + 1
        E = 1

    Task_Button = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = Task,activebackground='#151D33',relief = "flat")
    Task_Button.place(x = 16, y = 103,width = 52,height = 42)

    Task_Button.bind ('<Enter>',onButton3)
    Task_Button.bind('<Leave>',leaveButton3)
    Task_Button.bind ('<Button>',Pressed3)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
  
    # Button 4 (Main Menu Button)

    def onButton4(X): # Hover Effect On
        global E
        if E == 1:        
            MainMenu_Button['image'] = HHimg4

    def leaveButton4(X): # Hover Effect Off
        global E
        if E == 1:
            MainMenu_Button['image'] = img4

    def Pressed4(X): # Button Press

        Mic_Button.configure(image = img0)   
        Settings_Button.configure(image = img1)   
        Security_Button.configure(image = img2)   
        Task_Button.configure(image = img3)   
        MainMenu_Button.configure(image = Himg4)  
        global A
        global B
        global C
        global D
        global E
        A = 1
        B = 1
        C = 1
        D = 1
        E = E + 1

    MainMenu_Button = Button(image = Himg4,borderwidth = 0,highlightthickness = 0,command = MainMenu,activebackground='#151D33',relief = "flat")
    MainMenu_Button.place(x = 16, y = 63,width = 52,height = 42)

    global E
    E = 2 # To Make sure the Main Menu section stays highlighted

    MainMenu_Button.bind ('<Enter>',onButton4)
    MainMenu_Button.bind('<Leave>',leaveButton4)
    MainMenu_Button.bind ('<Button>', Pressed4)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #_____Startup Loading Screen_____#

    NeoStartup = PhotoImage(file = f"GUI Images\\NeoStartup.png")
    Loading = Label(window, bg = "#181818", height = 300,width = 600,  image = NeoStartup, highlightthickness = 0,relief = "ridge", borderwidth = 0)
    Loading.pack()

    def verify():
        psw = pass_entry.get()

        if psw == '1234':
            Loading.destroy()
            StartNEO_Btn.destroy()
            MainMenu()
        else:
            sys.exit()

        Loading.destroy()
        StartNEO_Btn.destroy()
        MainMenu()

    pass_entry = Entry(bd = 0,bg = "#ececec",highlightthickness = 0, font = FontLogin, show="*")
    pass_entry.place(x = 184, y = 198,width = 232,height = 26)

    StartNEO_IMG = PhotoImage(file = f"GUI Images\\StartNEO.png")
    StartNEO_Btn = Button(image = StartNEO_IMG,borderwidth = 0,highlightthickness = 0,command = verify,activebackground='#151D33',relief = "flat")
    StartNEO_Btn.place(x = 236, y = 247,width = 128,height = 36)
    
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate)) # Centralize Main Window
    window.resizable(False, False)
    window.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    MainWindow()