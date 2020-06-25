from pytube import YouTube
from tkinter import *
import threading


class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.thread = threading.Thread(target = self.download)
        self.initUI()


    def initUI(self):
        self.pack(fill = BOTH, expand = True)

        self.frame1 = Frame(self)
        self.frame1.pack()

        self.frame2 = Frame(self)
        self.frame2.pack(fill = X, padx = 10, pady = 40)

        self.frame3 = Frame(self)
        self.frame3.pack()

        self.frame4 = Frame(self)
        self.frame4.pack()


        Label(self.frame1, text = "YouTube", font = "ComicSans 20", fg = "red").pack()

        Label(self.frame2, text = "Url: ", font = "ComicSans 12").grid(row = 0, column = 0, padx = (0, 10))

        self.link = Entry(self.frame2, width = 50)
        self.link.grid(row = 0, column = 1)

        button = Button(self.frame3, text = "Fetch", font = "ComicSans 12", command = self.fetch)
        button.pack()

        self.display = Listbox(self.frame4, selectbackground = "green", activestyle = "none", height = 10, width = 30)

    def fetch(self):
        url = self.link.get()
        yt = YouTube(url)
        self.videos = yt.streams.all()

        self.display.grid(row = 0, column = 0, pady = (30, 0))
        self.select = Button(self.frame4, text = "Select", font = "ComicSans 12", command = self.find)
        self.select.grid(row = 0, column = 1, padx = 30)
        root.geometry("400x400+450+50")

        for index, video in enumerate(self.videos):
            self.display.insert("end" ,f"{index + 1}: {video.mime_type}, {video.resolution}\n")

    def find(self):
        name = self.display.get(ACTIVE)
        index = int(name.split(":")[0]) - 1

        self.video = self.videos[index]
        self.thread.start()



    def download(self):
        link = "C:\\Users\\Muhammed Fatih\\Downloads\\Videos"
        self.video.download(link)





if __name__ == '__main__':
    root = Tk()
    app = GUI(root)
    root.title("Video Downloader")
    root.geometry("400x200+450+50")
    root.mainloop()