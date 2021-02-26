from tkinter import *
import pytube
import os

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("YouTube Downloader")

dir_path = os.path.dirname(os.path.realpath(__file__))

run = True

dir_name = 'Downloaded Videos'

if not os.path.exists(dir_name):
    os.makedirs(dir_name)

Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()

link = StringVar()

Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)


def Downloader():
    if run:
        try:
            pytube.YouTube(link.get()).streams.get_highest_resolution().download(dir_path + '\Downloaded Videos')
            Label(root, text='DOWNLOADING..', font='arial 15').place(x=180, y=210)
            Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)
        except pytube.exceptions.RegexMatchError:
            Label(root, text='No Video Link/ Invalid Video Link', font='arial 15', fg='red').place(x=100, y=220)


Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, command=Downloader).place(x=180,
                                                                                                            y=150)

root.mainloop()
