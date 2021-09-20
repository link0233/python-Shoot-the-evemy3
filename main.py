from tkinter import *
from Covers.covers_main import *
import time

class main(Canvas):
    def __init__(self,width=1000,height=700):
        self.root=Tk()
        self.root.title('shoot-the-evemy')
        super(main,self).__init__(self.root,width=width,height=height,bg='#ffaaff')
        self.pack()

        self.bind('Motion',)

        time.sleep(1)
        self.cover=cover(self)
        self.cover.Loading(self.root,time)

        self.bind('<Motion>',self.mot)
        self.x=0
        self.y=0

        while True:
            self.cover.loop(self.x,self.y)
            self.root.update()
            time.sleep(0.01)

        self.root.mainloop()

    def mot(self,event):
        self.x=event.x
        self.y=event.y
if __name__=='__main__':
    main()