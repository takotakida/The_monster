import tkinter as tk
import maap1
import pygame as pg

if __name__ == "__main__":

    pg.init()
    test_sound = pg.mixer.Sound("stage1.mp3")
    test_sound.play(-1)

    root = tk.Tk()
    root.title("main")
    root.resizable(False,False)

    def click_start():
        root.destroy()
        maap1.plaay()

    def click_exit():
        root.destroy()

    img = tk.PhotoImage(file = "start.png")

    canvas = tk.Canvas(root,width= 600,height=450)
    canvas.pack()
    canvas.create_image(300,225, image = img)

    label = tk.Label(root,text = "game start",font = ("System",26))
    label.place(x = 225,y = 175)

    button1 = tk.Button(root,text = "start", font = ("System",24),command=click_start,bg = "lightgreen")
    button1.place(x = 150,y = 240)


    button2 = tk.Button(root,text = "exit", font = ("System",24),command=click_exit,bg = "lightgreen")
    button2.place(x = 350,y = 240)

    root.mainloop()

