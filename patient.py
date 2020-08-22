import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import datetime
import os
root = Tk()
root.title("Patient Health Monitoring System") 
now = datetime.datetime.now()
f = open("values1.txt", "r")
patient_name=[]
patient_id=[]
def details():
    global pid
    global name
    global id
    global btn
    global pname
    global entid
    global entname
    get_pid.destroy()
    get_entid.destroy()
    get_btn.destroy()
    pid.destroy()
    pname.destroy()
    entid.destroy()
    entname.destroy()
    reg.destroy()
    btn.destroy()
    
    fetch_line1.destroy()
    fetch_line2.destroy()
    fetch_line3.destroy()
    fetch_line4.destroy()
    fetch_line5.destroy()
    fetch_line6.destroy()
    
    wel.destroy()
    reg.destroy()

    id=tk.StringVar()
    pid=tk.Label(root, fg= 'black')
    pid.config(text="Patient ID: ", font=("Times New Roman", 15))
    pid.place(x=400, y=320)

    entid = tk.Entry(root, textvariable =id)
    entid.place(x=500,y=320)

   
    name=tk.StringVar()
    pname=tk.Label(root, fg= 'black')
    pname.config(text="Patient Name:", font=("Times New Roman", 15))
    pname.place(x=680, y=320)

    entname = tk.Entry(root, textvariable = name)
    entname.place(x=820,y=320)
    btn = Button(root, text ='Register', command = register)
    btn.place(x=610,y=400)

def register():
    global patient_id
    global patient_name
    global reg

    wel.destroy()

    patient_id.append(id.get())
    patient_name.append(name.get())
   
    pid.destroy()
    pname.destroy()
    entid.destroy()
    entname.destroy()
    btn.destroy()
    reg=tk.Label(root, fg= 'orange')
    reg.config(text="Registered Successfully!!!! ", font=("Times New Roman", 25))
    reg.place(x=480,y=380)

    


def getdetails():
    global get_entid
    global get_id
    global get_pid
    global get_btn
    wel.destroy()
    fetch_line1.destroy()
    fetch_line2.destroy()
    fetch_line3.destroy()
    fetch_line4.destroy()
    fetch_line5.destroy()
    fetch_line6.destroy()
    pid.destroy()
    pname.destroy()
    entid.destroy()
    entname.destroy()
    reg.destroy()
    btn.destroy()
    
    get_id=tk.StringVar()
    get_pid=tk.Label(root, fg= 'black')
    get_pid.config(text="Enter Patient ID: ", font=("Times New Roman", 15))
    get_pid.place(x=440, y=300)
    
    get_entid = tk.Entry(root, textvariable =get_id)
    get_entid.place(x=580,y=300)
    get_btn = Button(root, text ='Search', command = fetch)
    get_btn.place(x=740,y=300)

    
def fetch():
    wel.destroy()
    global fetch_line1
    global fetch_line2
    global fetch_line3
    global fetch_line4
    global fetch_line5
    global fetch_line6
    fetch_line1.destroy()
    fetch_line2.destroy()
    fetch_line3.destroy()
    fetch_line4.destroy()
    fetch_line5.destroy()
    fetch_line6.destroy()
    
   
    fn=get_id.get()
    fname='patients_data/'+fn+'.txt'
    f=open(fname,'r')
    line=f.readline()
    fetch_line1=tk.Label(root, fg= 'black')
    fetch_line1.config(text=line, font=("Times New Roman", 15))
    fetch_line1.place(x=440, y=380)
    
    line=f.readline()
    fetch_line2=tk.Label(root, fg= 'black')
    fetch_line2.config(text=line, font=("Times New Roman", 15))
    fetch_line2.place(x=440, y=410)
    
    line=f.readline()
    fetch_line3=tk.Label(root, fg= 'black')
    fetch_line3.config(text=line, font=("Times New Roman", 15))
    fetch_line3.place(x=440, y=440)
    
    line=f.readline()
    fetch_line4=tk.Label(root, fg= 'black')
    fetch_line4.config(text=line, font=("Times New Roman", 15))
    fetch_line4.place(x=440, y=470)
    
    line=f.readline()
    fetch_line5=tk.Label(root, fg= 'black')
    fetch_line5.config(text=line, font=("Times New Roman", 15))
    fetch_line5.place(x=440, y=500)
    
    line=f.readline()
    fetch_line6=tk.Label(root, fg= 'black')
    fetch_line6.config(text=line, font=("Times New Roman", 15))
    fetch_line6.place(x=440, y=530)
    
    
    f.close
    
def upload():
    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()
    drive = GoogleDrive(g_login)
    f = open("values1.txt", "r")
    limit=4
    i=1
    l=[]
    while True:
        for j in range(i,limit+1):
            line=f.readline()
            l.append(line)        
        i=limit+1
        if line!='':
            limit+=4
        else:
            break
    i=0
    j=0
    while i<=len(l):
        temp=l[i]
        pulse=l[i+1]
        ECG_value=l[i+2]
        glucose=l[i+3]      
        s1='Patient ID:'+str(patient_id[j])+'\t\t'
        s2='Patient Name:'+patient_name[j]+'\n--------------------------------------------------------------------\n'
        s3='Temperature (*c)\t :\t'+str(temp)
        s4='Pulse/SPO2       \t:\t'+str(pulse)
        s5='ECG value        \t:\t'+str(ECG_value)
        s6='Glucose (mg/dl)  \t:\t'+str(glucose)
        s=s1+s2+s3+s4+s5+s6
        fname=str(patient_id[j])
        f= open("patients_data/"+fname+".txt","w+")
        f.write(s)
        f.close() 
        file1 = drive.CreateFile({'title': fname})
        file1.SetContentString(s)
        file1.Upload()
        i+=4        
        j+=1
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.resizable(width = True, height = True)


'''canvas = tk.Canvas(root, width = 1080, height = 800)
canvas.pack()
photo =ImageTk.PhotoImage(Image.open('13.png'))
canvas.create_image(0, 0,  anchor=NW, image=photo)'''

lbl=tk.Label(root, fg= 'blue')
lbl.config(text="PATIENT HEALTH MONITORING SYSTEM", font=("Times New Roman", 41))
lbl.place(x=220, y=55)
wel=tk.Label(root, fg= 'red')
wel.config(text="Welcome!!!!", font=("Monotype Corsiva",50))
wel.place(x=530, y=350)

lbl=tk.Label(root, fg= 'green')
lbl.config(text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|", font=("Monotype Corsiva",40))
lbl.place(x=240, y=120)

lbl=tk.Label(root, fg= 'green')
lbl.config(text="--------------------------------------------------------------------", font=("Monotype Corsiva",60))
lbl.place(x=0, y=120)

lbl=tk.Label(root, fg= 'green')
lbl.config(text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", font=("Monotype Corsiva",20))
lbl.place(x=0, y=0)

timedate='Date :'+now.strftime("%Y-%m-%d")
lbl=tk.Label(root, fg= 'black')
lbl.config(text=timedate, font=("Times New Roman", 18))
lbl.place(x=1150, y=190)

btn = Button(root, text ='Upload', command = upload)
btn.place(x=150,y=370)
btn = Button(root, text ='Analysis', command = getdetails)
btn.place(x=150,y=320)
btn = Button(root, text ='Register', command = details)
btn.place(x=150,y=270)
lbl1=tk.Label(root, fg= 'grey')
lbl1.config(text="Project Associates:\n       1. V. Haneela\n\t2. k.Harsha Deepika \n\t3. M.Lakshmi Akhila", font=("Copperplate Gothic Light", 15))
lbl1.place(x=990, y=550)
#print(patient_id)
p_name=''
reg = Button(root, text ='Registered!!, Add another', command = details)
entname = tk.Entry(root, textvariable = p_name)
pid=tk.Label(root, fg= 'grey')
pname=tk.Label(root, fg= 'grey')
entid = tk.Entry(root, textvariable =id)
btn = Button(root, text ='Register', command = register)
get_pid=tk.Label(root, fg= 'grey')
get_id=tk.StringVar()
get_entid = tk.Entry(root, textvariable =get_id)
get_btn = Button(root, text ='Search', command = fetch)
fetch_line1=tk.Label(root, fg= 'grey')
fetch_line2=tk.Label(root, fg= 'grey')
fetch_line3=tk.Label(root, fg= 'grey')
fetch_line4=tk.Label(root, fg= 'grey')
fetch_line5=tk.Label(root, fg= 'grey')
fetch_line6=tk.Label(root, fg= 'grey')
root.mainloop()


