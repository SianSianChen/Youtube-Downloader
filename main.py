import tkinter as tk
from pytube import YouTube


def Download():
    global userURL
    global userPATH

    
    url = str(userURL.get())
    path = str(userPATH.get())

    YouTube(url).streams.first().download(output_path=path)

    Finishlb.config(text='enjoy your video!')


win = tk.Tk()
win.title('Youtube Downloader')
win.geometry('600x400+550+300')
win.iconbitmap('D:/Coding/source/git/Python/Pytube/icon.ico')
win.attributes('-topmost', 1)
win.config(bg='yellow')


titlelb = tk.Label()
titlelb.config(text='Youtube Downloader')
titlelb.config(bg='skyblue')
titlelb.config(font='Calibri 35')
titlelb.pack(fill='x')

URLEntrylb = tk.Label()
URLEntrylb.config(text="Video Link here:")
URLEntrylb.config(bg='yellow')
URLEntrylb.config(font='Arial 25')
URLEntrylb.pack(fill='x')

userURL = tk.Entry()
userURL.config(width=50)
userURL.pack()


PATHEntrylb = tk.Label()
PATHEntrylb.config(text="Video output path:")
PATHEntrylb.config(bg='yellow')
PATHEntrylb.config(font='Arial 25')
PATHEntrylb.pack(fill='x')

userPATH = tk.Entry()
userPATH.config(width=50)
userPATH.pack()


DownloadBtn = tk.Button()
DownloadBtn.config(text='Download')
DownloadBtn.config(bg='red')
DownloadBtn.config(font='Arial 30')
DownloadBtn.config(command=Download)
DownloadBtn.pack()




Finishlb = tk.Label()
Finishlb.config(bg='yellow')
Finishlb.config(font='微軟正黑體 20')
Finishlb.pack()







win.mainloop()