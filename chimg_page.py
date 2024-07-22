#python3.9
import tkinter as tk
import glob
from PIL import Image, ImageTk, ImageOps
import os
import keyboard
import tqdm
import time
import math
import threading
import webbrowser
import socket
from flask import Flask, render_template,request,url_for

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
       # print(path)

gy =5
def floatimg():
    x =0
    global gy,bim
    while True:
        gy =20+5*math.sin(math.radians(x))
        x+=2
        print(f"\r {x}:{gy}",end="")
        isinstances[bim].frame.place(x=5,y=5+gy)
        time.sleep(0.1)


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
                
                isinstances[bim].frame.place(x=5,y=5+gy)
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



app = Flask(__name__)


@app.route('/',methods=["GET"])
def select():

    return render_template("task.html")



@app.route('/pat/<val>',methods=["GET", "POST"])
def sel(val):
    global pressed,amax,bim,isinstances
    for i in isinstances:
        i.frame.place(x=5,y=5+gy)    
    for i in isinstances:
        i.frame.place_forget()
            
    isinstances[int(val)].frame.place(x=5,y=5+gy)
    print(isinstances[int(val)].path)
    return "<script>location.replace('../');</script>"
    


connect_interface = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
connect_interface.connect(("8.8.8.8", 80))
print("外部から接続する時のアドレス")
a = " http://"+connect_interface.getsockname()[0]+":5000"
print(a)
connect_interface.close()
def op():
    time.sleep(2)
    webbrowser.open(a)
    time.sleep(1)
    
    webbrowser.open("http://127.0.0.1:5000")

def flaskapp():
        threading.Thread(target=op).start()
        app.run(debug=False,port=5000,host="0.0.0.0")
    
print("==========================================")

if __name__ == "__main__":
    imgs =glob.glob("static/img/*.png")
    imgs +=glob.glob("static/img/*.jpg")
    with open("templates/task.html","w",encoding="utf-8") as f:
        f.write("""<!DOCTYPE html>    <html>    <style>
    
    .imgnode {
    width: 213px;
    height: auto;
    }
    </style>
    <body>
    <!-- 画像を重ねて配置 --><div style="position: relative;">""")
        imgp =[]
        for i in range(len(imgs)):
            y =imgs[i].replace(r"\\","/")
            print(y)
            f.write(f'<input class="imgnode" type="image" name="画像ボタンの名前" onclick="location.href=\'../pat/{i}\'" src="/{y}" alt="Example Image">')
            imgp.append(y)
        f.write("</div>    </body>    </html>")

    threading.Thread(target=flaskapp,daemon=True).start()
    root = tk.Tk()
    #app.
    root.geometry("500x620")
    #os.chdir("img")
    #os.chdir("..")
    print(imgs)
    global amax,bim,isinstances
    amax =0
    isinstances =[]
    for i in tqdm.tqdm(imgp):
        print(i)
        time.sleep(0.1)
        isinstances.append(test(root,i))
        amax +=1
    print("==========================================")
    for bim in tqdm.tqdm(range(amax)):
        time.sleep(0.1)
        isinstances[bim-1].frame.place_forget()
        #isinstances[bim].frame.place(x=0,y=0)

    bim=0
    #threading.Thread(target=floatimg,daemon=True).start()
    #keyboard.hook(on_shift_event)

    root.mainloop()
    keyboard.unhook_all()