#python3.9
import tkinter as tk
import glob
from PIL import Image, ImageTk, ImageOps
import os
import keyboard
import tqdm
import time
base =os.getcwd()
#imgpath =
class test:
    def __init__(self,window,path) -> None:
        self.im =Image.open(path)
        self.path =path
        self.w, self.h = self.im.size
        #self.im.resize(int(self.w/2), int(self.h/2))
        #self.w, self.h = self.im.size
        self.frame= tk.Frame(window)
        self.frame.place(x=10,y=10)
        self.canvas = tk.Canvas(self.frame, width = self.w, height = self.h)
        self.canvas.pack()


        self.img =ImageTk.PhotoImage(self.im) #tk.PhotoImage(file = path)
        self.canvas.create_image(self.w/2, self.h/2, image = self.img)
        print(path)
def on_shift_event(e):
    global pressed,amax,bim,isinstances
    pressed=False
    if e.event_type == keyboard.KEY_DOWN:
        if e.name in "space":
            if pressed:
                pass
            else:
                pressed = True
                print(e.name,"T")
                #wid[int(e.name)-1].Plus()
                bim+=1
                if bim>=amax:
                    bim=0
                isinstances[bim-1].frame.place_forget()
                isinstances[bim].frame.place(x=5,y=5)
                print(isinstances[bim].path)
                """
        if e.name in ["f13","f14","f15","f16","f17","f18","f19","f20","f21","f22","f23","f24"]:
            if pressed:
                pass
            else:
                x =e.name[1:]
                
                pressed = True
                print(e.name,"T")
                #wid[int(e.name)-1].Plus()
                for i in isinstances:
                    i.frame.place_forget()
                isinstances[int(x)-13].frame.place(x=5,y=5)
                print(isinstances[bim].path)
            """

        else:
            print(e.name,"F")        
    elif e.event_type == keyboard.KEY_UP:
       # if e.name in Rlist:
            pressed = False



if __name__ == "__main__":
    app = tk.Tk()
    #app.
    app.geometry("500x620")
    #os.chdir("img")
    imgs =glob.glob("img/*.png")
    imgs +=glob.glob("img/*.jpg")
    #os.chdir("..")
    print(imgs)
    global amax,bim,isinstances
    amax =0
    isinstances =[]
    for i in tqdm.tqdm(imgs):
        time.sleep(0.1)
        isinstances.append(test(app,i))
        amax +=1
    print("==========")
    for bim in tqdm.tqdm(range(amax)):
        time.sleep(0.1)
        isinstances[bim-1].frame.place_forget()
        #isinstances[bim].frame.place(x=0,y=0)

    bim=0
    
    keyboard.hook(on_shift_event)

    app.mainloop()
    keyboard.unhook_all()