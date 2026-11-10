import customtkinter
import os
from pathlib import Path
from tkinter import filedialog
import subprocess
import threading
main_path=os.path.dirname(os.path.abspath(__file__))
path=Path(main_path.replace("\\","/")+"/servers/")
selectedpath1=[path]
readingwriting=False

format=['mp4']
if readingwriting==True:
  with open("pathselected1.txt", "r") as file:
        content = file.read()
        selectedpath1[0]=content
  os.remove ("pathselected1.txt")



subprocess.run("yt-dlp -U", shell=True)
app=customtkinter.CTk()
app.title ('video downloader')
app.geometry("540x540")
app.resizable(False, False)
app.grid_columnconfigure(0, weight=2)
title=customtkinter.CTkLabel(app, text=" ", width=350, height=40 )
title.grid(row=0, column=0, pady=10)

textbox = customtkinter.CTkEntry(app, placeholder_text="link of video:", height=20
                                 , width=200
                                 ,corner_radius=20)
textbox.grid(row=1, column=0, padx=(10,5), pady=10)


     
typeoffile=customtkinter.CTkOptionMenu(app,
                                       values=["MP4","MKV", 'WebM', "MP3",'M4A','OGG'],
                                       width=40,
                                       height=20,
                                       
corner_radius=20)

typeoffile.grid(row=1, column=1, padx=(5,10), pady=10)
progress=customtkinter.CTkProgressBar(app,orientation="horizontal", mode="determinate", determinate_speed=50 )
progress.grid(row=2, column=0,pady=30)
progress.set(0)
recode_var = customtkinter.StringVar(value="off")
recode = customtkinter.CTkCheckBox(app, text="recode video to wanted format", 
                                   variable=recode_var, onvalue="on", offvalue="off")
recode.grid(row=5, column=0, pady=10)
def buttonclicked():
    
    title.configure(text=" ")
    app.update_idletasks()
    proccess=subprocess.run('yt-dlp --simulate '+str(textbox.get()), shell=True
                   ,capture_output=True,
                   text=True)
    if proccess.returncode == 0:
        print("download sucessful")
        title.configure(text="downloading...")
        progress.set(0)
        progress.start()
        app.update_idletasks()
        command=['hello']
        #command for normal 
        command1="yt-dlp -f mp4 "+textbox.get()
        command2="yt-dlp -f mkv "+textbox.get()
        command3="yt-dlp -f webm "+textbox.get()
        command4="yt-dlp -f mp3 "+textbox.get()
        command5="yt-dlp -f m4a "+textbox.get()
        command6='yt-dlp -f ogg '+textbox.get()
        #commands for recode
        command12 = f'yt-dlp "{textbox.get()}" -P "{selectedpath1[0]}" --recode-video mp4'
        command22= f'yt-dlp "{textbox.get()}" -P "{selectedpath1[0]}" --recode-video mkv'
        command32 = f'yt-dlp "{textbox.get()}" -P "{selectedpath1[0]}" --recode-video webm'
        command42 = f'yt-dlp "{textbox.get()}" -P "{selectedpath1[0]}" --extract-audio --audio-format mp3'
        command52 = f'yt-dlp "{textbox.get()}" -P "{selectedpath1[0]}" --extract-audio --audio-format m4a'
        command62 = f'yt-dlp "{textbox.get()}" -P "{selectedpath1[0]}" --extract-audio --audio-format ogg'
        if typeoffile.get()=='MP4':
             if recode_var=="off":
                command[0]=command1
             else:
                  command[0]=command12
        elif typeoffile.get()=='MKV':
             if recode_var=="off":
                command[0]=command2
             else:
                  command[0]=command22
        elif typeoffile.get()=='WebM':
             if recode_var=="off":
                command[0]=command3
             else:
                  command[0]=command32
        elif typeoffile.get()=='MP3':
             if recode_var=="off":
                command[0]=command4
             else:
                  command[0]=command42
        elif typeoffile.get()=='M4A':
             if recode_var=="off":
                command[0]=command5
             else:
                  command[0]=command52
        elif typeoffile.get()=='OGG':
             if recode_var=="off":
                command[0]=command6
             else:
                  command[0]=command62
        istaskcoplete=["hi"]
        def task01():
             subprocess.run(command[0],shell=True)
             istaskcoplete[0]="done"
        def task02():
             app.update_idletasks()
             if istaskcoplete[0]=="done":
               progress.stop()
               progress.set(1)
        app.update_idletasks()
        
        app.update_idletasks()
        thread1 = threading.Thread(target=task01)
        thread2 = threading.Thread(target=task02)
        thread1.start()
        thread2.start()
        textbox.delete(0, customtkinter.END)
        app.update_idletasks()
        title.configure(text="video downloaded")
        
    else:
        print ("download failed retry")
        textbox.delete(0, customtkinter.END)
        title.configure(text="video not downloaded retry")

button=customtkinter.CTkButton(app, text='download video', command=buttonclicked)
button.grid (row=3, column=0, padx=45)
def select_folder():
    # This opens the popup window
    selected = filedialog.askdirectory()
    selectedpath1[0]=selected
    path_of_videobtn.configure(text="save to"+selected)
    if readingwriting==True:
      with open ('pathselected1.txt' ,'w')as f:
                  f.write (selected)
    app.update_idletasks()

path_of_videobtn=customtkinter.CTkButton(app, text=selectedpath1[0], command=select_folder)
path_of_videobtn.grid(row=4, column=0, padx=45, pady=10)
app.mainloop()
