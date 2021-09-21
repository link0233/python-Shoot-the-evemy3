from tkinter import *
from Covers.covers_main import *
import time
from player.player import player

class main(Canvas):
    def __init__(self,width=1000,height=700):
        self.root=Tk()
        self.root.title('shoot-the-evemy')
        super(main,self).__init__(self.root,width=width,height=height,bg='#ffaaff')
        self.pack()

        time.sleep(1)
        self.cover=cover(self)
        self.cover.Loading(self.root,time)

        self.player=player(self)

        self.bind('<Motion>',self.mot)
        self.bind('<Button-1>',self.button1)
        self.x=0
        self.y=0
        self.but1=0

        while True:
            self.cover.loop(self.x,self.y,self.but1)

            if self.cover.delete==1:
                self.start()

            self.root.update()
            time.sleep(0.01)
            if self.but1==1:
                self.but1==0

        self.root.mainloop()

    def mot(self,event):
        self.x=event.x
        self.y=event.y

    def button1(self,event):
        self.x=event.x
        self.y=event.y
        self.but1=1

    def start(self):
        self.player_image=PhotoImage(file='platyer_image.png')
        self.player.start(self.player_image)

if __name__=='__main__':
    main()