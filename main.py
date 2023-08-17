#coding=gbk
from tkinter import Tk, Label, Button
from pydub import AudioSegment
import os
import tkinter
import tkinter.ttk
import shutil
import json
import math
from moviepy.editor import *



'''
class ProcessBar():

    def __init__(self):        
        self.process = ttk.Progressbar(root, length=200, mode="determinate",maximum=100,orient=tk.HORIZONTAL)   
        self.process.place(x=100, y=10)
 
    def value(self, per):
        self.process["value"]  = per
        root.update()
    '''

        
    



class GUI:
    def __init__(self, master):
        self.master = master





        sw = master.winfo_screenwidth()
        # 得到屏幕宽度
        sh = master.winfo_screenheight()

        # 得到屏幕高度
        ww = 450
        wh = 160

        x = (sw - ww) / 2
        y = (sh - wh) / 2
        master.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

        master.title("Mhbot to Malody tool by  Funoke")


        self.label = Label(master, text="请先把相应文件放入工作台文件夹“Bench”\n工作台使用规则：\n1.Macro文件夹里面放入MHbot Vanilla模式录制脚本导出的json文件\n2.video文件夹里放入标准的showcase视频文件\n3.点击clear可以清除工作台内的所有文件")
        self.label.pack()

        self.greet_button = Button(master, text="BOOM", command=self.greet)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Clear", command=self.clear)
        self.greet_button.pack()

    def clear(self):
        croot = str(os.getcwd())+str("\\Bench")
        print("hellp")
        if os.path.exists(croot+"\\Bench\\Macro"):
            shutil.rmtree(croot+"\\Bench\\Macro")
            os.mkdir(croot+"\\Bench\\Macro")
        if os.path.exists(croot+"\\Bench\\Video"):
            shutil.rmtree(croot+"\\Bench\\Video")
            os.mkdir(croot+"\\Bench\\Video")    






    def greet(self):
        croot = str(os.getcwd())+str("\\Bench")
        root1 = tkinter.Tk()


        '''
        root1.title("Progress Bar")
        root1.geometry('150x25')
        progressbarOne = tkinter.ttk.Progressbar(root1)
        progressbarOne.pack(side=tkinter.TOP)
        '''


        videopath = os.walk(str(croot+"\\Video"))
        for dirpath,dirnames,filenames in videopath:
            videoname = str(filenames[0])
        print(str(croot+"\\Video\\")+str(videoname))
        video = AudioSegment.from_file(str(croot+"\\Video\\")+str(videoname))


        if os.path.exists(str(os.getcwd())+"\\Result\\_temp_1692000000"):
            shutil.rmtree(str(os.getcwd())+"\\Result\\_temp_1692000000")
        os.makedirs(str(os.getcwd())+"\\Result\\_temp_1692000000")
        f = open(str(os.getcwd())+"\\Result\\_temp_1692000000\\1692000000.mc","w")


        audio = video.export(str(os.getcwd())+"\\Result\\_temp_1692000000\\"+"1692000000.ogg", format='ogg')
        
        cap = str(croot+"\\Video\\")+str(videoname)
        video = VideoFileClip(cap)
        video.write_videofile(str(os.getcwd())+"\\Result\\_temp_1692000000\\"+"1692000000.mp4",codec='h264',bitrate='3000k',ffmpeg_params=['-s','1280x720','-r','31','-ar','48000','-ab','320k','-pix_fmt','yuv420p'])
        
        
        #video = video.export(str(os.getcwd())+"\\Result\\"+"video.mp4", format='mp4',parameters=ffmpeg -s 640*480 -b 800k)
        




        macropath = os.walk(str(croot+"\\Macro"))
        for dirpath,dirnames,filenames in macropath:
            macroname = str(filenames[0])
        

        fr = open(str(croot+"\\Macro\\")+macroname, 'r')
        content = fr.read()
        a = json.loads(content)
        #print(len(a['events']))

        fps = float(a['meta']['fps'])
        wholefps = int(a['events'][int(len(a['events']))-1]['frame'])
        #print (wholefps)


        s=0
        #p1是player1按下的frame ; p2是抬起
        p1 =  []

        

        while s < int(len(a['events'])):
            if str('p2')in str(a['events'][s]):
                s=s+1
            else:
                if "True" in str(a['events'][s]['down']):
                    ap=int(a['events'][s]['frame'])
                    p1.append(ap)
                s=s+1

        s=0
        p2 =  []
        while s<(len(a['events'])):
            #print(int(a['events'][s]['frame']))
            if str('p2')in str(a['events'][s]):
                s=s+1
            else:
                if "False" in str(a['events'][s]['down']):
                    ap=int(a['events'][s]['frame'])
                    p2.append(ap)
                s=s+1

                


        #p3是player3按下的frame ; p4是抬起
        s=0
        p3 =  []
        while s<(len(a['events'])):
            #print(int(a['events'][s]['frame']))
            if "p2"in str(a['events'][s]):
                if "True" in str(a['events'][s]['down']):
                    ap=int(a['events'][s]['frame'])
                    p3.append(ap)
                    s=s+1
                else:
                    s=s+1
            else:
                s=s+1
        s=0
        p4 =  []
        while s<(len(a['events'])):
            #print(int(a['events'][s]['frame']))
            if "p2"in str(a['events'][s]):
                if "False" in str(a['events'][s]['down']):
                    ap=int(a['events'][s]['frame'])
                    p4.append(ap)
                    s=s+1
                else:
                    s=s+1
            else:
                s=s+1

        #补充：导入视频

        #开始导出Malody谱


        mc='{\n"meta":{\n"$ver":0,\n"creator":"PowerPlant",\n"background":"",\n"version":"",\n"video":"1692000000.mp4",\n"id":0,\n"mode":0,\n"time":1692000000,\n"song":{\n"title":"_temp_1692000000",\n"artist":"PowerPlant","id":0},\n"mode_ext":{"column":4,"bar_begin":0}},\n"time":[{"beat":[0,0,1],"bpm":300.0}],"effect":[],\n"note":[\n'
        #"{\n"+'"meta":{\n'+'"$ver":0,\n'+'"creator": "PowerPlant",\n'+'"background": "bg.jpg",\n'+'"version": "bot to malody",\n'+'"video":"video.mp4"\n'+'"preview":30\n'+'"id":0,\n'+'"mode":0,\n'+'"time": 1600000000,\n'+'"song":\n{\n'+'"title":"NA"\n'+'"artist":"You",\n"id":0,\n"titleorg":"NA",\n"artistorg":"You"\n},\n'+'"mode_ext":{"column":4,"bar_begin":0}},\n'+'"time":[{"beat":[0,0,1],"bpm":900.0}],\n'+'"effect":[],\n'+'"note": [\n'
        s=0

        #player1
        c1=[]
        c2=[]
        while s<(len(p1)):
            c10=math.ceil((float(p1[s]))/(float(a['meta']['fps']))*60)
            c20=math.floor((float(p2[s]))/(float(a['meta']['fps']))*60)
            if c10<c20:
                c1.append(c10)
                c2.append(c20)
                
            else:
                c1.append(c10)
                c2.append(c10)
            s=s+1
        s=0
        #player2
        c3=[]
        c4=[]
        while s<(len(p3)):
            c30=math.ceil((float(p3[s]))/(float(a['meta']['fps']))*60)
            c40=math.floor((float(p4[s]))/(float(a['meta']['fps']))*60)
            if c30<c40:
                c3.append(c30)
                c4.append(c40)
            else:
                c3.append(c30)
                c4.append(c30)
            s=s+1



        s=0
        while s<len(c1):
            mc1='{"beat":['+str(math.floor(c1[s]/12))+","+str((math.floor(c1[s])%12))+",12]"    +    ',"endbeat":['+str(math.floor(c2[s]/12))+","+str((math.floor(c2[s])%12))+',12],"column":1},\n'
            mc = mc+mc1

            s=s+1

        s=0

        while s<len(c3):
            mc2='{"beat":['+str(math.floor(c3[s]/12))+","+str((math.floor(c3[s])%12))+",12]"    +    ',"endbeat":['+str(math.floor(c4[s]/12))+","+str((math.floor(c4[s])%12))+',12],"column":2},\n'
            mc=mc+mc2
            s=s+1

        mc=mc+'{"beat":[0,0,1],\n"sound":"1692000000.ogg",\n"vol":100,\n"offset":0,\n"type":1}],\n"extra":{"test":{"divide":4,"speed":100,"save":0,"lock":0,"edit_mode":0}}}'
        #'{"beat":[0,0,1],"sound":"music.ogg","vol":100,"offset":513,"type":1}],"extra":{"test":{"divide":4,"speed":100,"save":0,"lock":0,"edit_mode":0}}}'
        print("谱面文件已生成")

        f.write(mc)
        f.close()












        


        
root = Tk()
my_gui = GUI(root)
root.mainloop()
